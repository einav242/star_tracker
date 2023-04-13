import os

from scipy.optimize import linear_sum_assignment
from scipy.spatial import distance_matrix
from skimage.feature import blob_log
from skimage.color import rgb2gray, rgb2yuv
import numpy as np
import cv2


def find_coordinates(img_path, output_path=None):
    # Read the image using OpenCV
    image = cv2.imread(img_path)
    # Convert the image to YUV color space and use the Y channel only
    yuv_image = rgb2yuv(image)
    yuv_image = yuv_image[:, :, 0]
    # Detect stars using blob detection with Laplacian of Gaussian (LoG) method
    blobs_log = blob_log(yuv_image, max_sigma=30, num_sigma=10, threshold=.1)
    # For each detected blob, calculate its brightness and store its coordinates
    coordinates = []
    for i, blob in enumerate(blobs_log):
        y, x, r = blob
        brightness = np.mean(yuv_image[int(y - r):int(y + r), int(x - r):int(x + r)])
        coordinates.append((x, y, r, brightness))
    if output_path is not None:
        with open(output_path, 'w') as f:
            for result in coordinates:
                f.write(f"{result[0]},{result[1]},{result[2]},{result[3]}\n")
    return coordinates


def distance(point1, point2):
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def match_stars(img1_path, img2_path, output_path=None):
    """
    Finding star matches between two images using the RANSAC algorithm.

    :param img1_path: Path to the first image.
    :param img2_path: Path to the second image.
    :param output_path: (Optional) Path to write the output file containing the matching star pairs.
    :return: A list of tuples, where each tuple contains the coordinates and radius of a matching star in both images.
    """
    stars1 = np.array(find_coordinates(img1_path))
    stars2 = np.array(find_coordinates(img2_path))

    # Create a distance matrix between all stars in both images
    dist_matrix = distance_matrix(stars1[:, :2], stars2[:, :2])

    # Convert the distance matrix to a cost matrix for the linear sum assignment problem
    cost_matrix = (1 - dist_matrix / 50)

    # Solve the linear sum assignment problem
    row_ind, col_ind = linear_sum_assignment(-cost_matrix)

    # Create a list of matching star pairs
    matching_pairs = []
    for row, col in zip(row_ind, col_ind):
        # We will only add to the list the pairs whose matching cost is positive.
        if cost_matrix[row, col] > 0:
            matching_pairs.append((tuple(stars1[row]), tuple(stars2[col])))

    # Write the output file if a path is provided
    if output_path is not None:
        with open(output_path, "w") as file:
            for pair in matching_pairs:
                file.write(str(pair) + "\n")

    return matching_pairs


list_of_stars = []
for i in range(3046, 3063):
    file1 = "IMG_" + str(i) + ".jpg"
    file1 = os.path.join("data", file1)

    file2 = "IMG_" + str(i + 1) + ".jpg"
    file2 = os.path.join("data", file2)

    output = "output" + str(i) + ".txt"
    temp_list = match_stars(file1, file2, output)
    print(file1, "vs.", file2, "= ", temp_list)
    list_of_stars.append(temp_list)
