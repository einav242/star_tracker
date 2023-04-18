import os
import numpy as np
import cv2
from scipy.optimize import linear_sum_assignment
from scipy.spatial import distance_matrix

from star import Star


def find_coordinates(img_path, output_path=None):
    """
    This function finds the coordinates of stars in an image using image processing techniques.

    Parameters:
    img_path (str): The path of the image file.
    output_path (str): The path of the output file. If None, the function does not save the results.

    Returns:
    coordinates (list): A list of Star objects representing the stars found in the image.
    """
    # Load the image and convert it to grayscale
    image = cv2.imread(img_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to the image
    _, thresh = cv2.threshold(gray, 180, 220, cv2.THRESH_BINARY)

    # Find the contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize variables
    coordinates = []
    check = []
    count = 0

    # Loop through the contours
    for i, c in enumerate(contours):
        # Get the coordinates and size of the bounding rectangle around the contour
        x, y, w, h = cv2.boundingRect(c)

        # Calculate the radius of the circle that encloses the rectangle
        r = int((w + h) / 4)

        # Calculate the average brightness of the region inside the rectangle
        b = int(gray[y:y + h, x:x + w].mean())

        # Calculate the center coordinates of the rectangle
        x = x + w / 2
        y = y + h / 2

        # Create a Star object with the calculated parameters
        st = Star(x, y, r, b, count, image)

        # Check if the coordinates have already been added
        ans = (x, y)
        if ans in check:
            continue

        # Add the Star object to the list of coordinates
        coordinates.append(st)
        check.append(ans)
        count += 1

    # If an output path is provided, write the coordinates to a file
    if output_path is not None:
        with open(output_path, 'w') as f:
            for result in coordinates:
                f.write(f"{result.id},{result.x},{result.y},{result.r},{result.b}\n")

    # Return the list of coordinates
    return coordinates


def draw_image(img_path, coordinates):
    # Load image from file
    image = cv2.imread(img_path)

    # Draw circles on the image where there are stars
    for star in coordinates:
        cv2.circle(image, (int(star.x), int(star.y)), int(star.r) + 5, (0, 255, 255), 5)

    # Save the processed image to file
    filename = "%s_processed.jpg" % img_path
    cv2.imwrite(filename, image)
    cv2.destroyAllWindows()


def show_stars(filename_1, filename_2, matching, output_file):
    # Load images from file
    image1 = cv2.imread(filename_1)
    image2 = cv2.imread(filename_2)

    # Iterate over matching stars and draw circles and labels on both images
    for match in matching:
        star1 = match[0]
        star2 = match[1]

        # Draw circle and label on first image
        cv2.circle(image1, (int(star1.x), int(star1.y)), int(star1.r) + 5, (0, 255, 0), 5)
        cv2.putText(image1, "ID: " + star1.id, (int(star1.x) + int(star1.r) + 5, int(star1.y)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    2.5,
                    (0, 255, 0), 2)

        # Draw circle and label on second image
        cv2.circle(image2, (int(star2.x), int(star2.y)), int(star2.r) + 5, (0, 255, 0), 5)
        cv2.putText(image2, "ID: " + star2.id, (int(star2.x) + int(star2.r) + 5, int(star2.y)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    2.5,
                    (0, 255, 0), 2)

    # Resize second image to match the size of the first image, and concatenate the images side-by-side
    img2_resized = cv2.resize(image2, (image1.shape[1], image1.shape[0]))
    result = cv2.hconcat([image1, img2_resized])

    # Save the resulting image to file
    cv2.imwrite(output_file, result)
    cv2.destroyAllWindows()


# The function returns the distance between two stars.
def distance(point1, point2):
    return np.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)


def find_matching_stars(img1_path, img2_path, output_path=None):
    """
      Find matching pairs of stars between two input images.

      Parameters:
          - img1_path (str): path to the first image file
          - img2_path (str): path to the second image file
          - output_path (str, optional): path to output file to write matching pairs (default=None)

      Returns:
          - matching_pairs (list of tuples): list of matching star pairs between the two images,
              where each pair is a tuple of Star objects representing the corresponding stars in each image
      """
    # Find coordinates of stars in the first image
    stars1 = find_coordinates(img1_path)
    # Draw the first image with the found stars marked
    draw_image(img1_path, stars1)
    # Find coordinates of stars in the second image
    stars2 = find_coordinates(img2_path)
    # Draw the second image with the found stars marked
    draw_image(img2_path, stars2)
    # Compute the distance matrix between the star coordinates in the two images
    distances = distance_matrix(np.array([(s.x, s.y) for s in stars1]), np.array([(s.x, s.y) for s in stars2]))
    # Use the Hungarian algorithm to find the optimal matching between the stars in the two images
    row_ind, col_ind = linear_sum_assignment(distances)
    # Create a list of matching star pairs
    matching_pairs = []
    for r, c in zip(row_ind, col_ind):
        matching_pairs.append((stars1[r], stars2[c]))
    # Write the matching pairs to an output file if an output path is provided
    if output_path is not None:
        with open(output_path, "w") as file:
            for pair in matching_pairs:
                p = (pair[0].id, pair[1].id)
                file.write(str(p) + "\n")
    # Return the list of matching star pairs
    return matching_pairs


for i in range(3046, 3062):
    file1 = "IMG_" + str(i) + ".jpg"
    file1 = os.path.join("data", file1)
    file2 = "IMG_" + str(i + 1) + ".jpg"
    file2 = os.path.join("data", file2)
    output = "output" + str(i) + ".txt"
    output = os.path.join("result", output)
    temp_list = find_matching_stars(file1, file2, output)
    tmp = [(m[0].id, m[1].id) for m in temp_list]
    print(file1, "vs.", file2, "= ", tmp)
    filename1 = "%s_processed.jpg" % file1
    filename2 = "%s_processed.jpg" % file2
    output_img = "output" + str(i) + ".jpg"
    output_img = os.path.join("result", output_img)
    show_stars(filename1, filename2, temp_list, output_img)
