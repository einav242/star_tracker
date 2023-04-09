from skimage.feature import blob_log
from skimage.color import rgb2gray
import numpy as np
import cv2


def find_coordinates(img_path, output_path=None):
    image = cv2.imread(img_path)
    gray = rgb2gray(image)

    blobs_log = blob_log(gray, max_sigma=30, num_sigma=10, threshold=.1)

    coordinates = []
    for i, blob in enumerate(blobs_log):
        y, x, r = blob
        brightness = np.mean(gray[int(y - r):int(y + r), int(x - r):int(x + r)])
        coordinates.append((x, y, r, brightness))
    if output_path is not None:
        with open(output_path, 'w') as f:
            for result in coordinates:
                f.write(f"{result[0]},{result[1]},{result[2]},{result[3]}\n")
    return coordinates


def distance(point1, point2):
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def match_stars(img1_path, img2_path, output_path=None):
    stars1 = find_coordinates(img1_path)
    stars2 = find_coordinates(img2_path)
    matching_pairs = []
    max_matching_score = 1
    for star1 in stars1:
        best_matching_score = max_matching_score
        matching_star = None

        for star2 in stars2:
            dist = distance(star1, star2)

            if dist < 50:
                matching_score = 1 - (dist / 50)

                if matching_score < best_matching_score:
                    best_matching_score = matching_score
                    matching_star = star2

        if matching_star is not None:
            matching_pairs.append((star1, matching_star))
            stars2.remove(matching_star)

    if output_path is not None:
        with open(output_path, "w") as file:
            for pair in matching_pairs:
                file.write(str(pair) + "\n")

    return matching_pairs


print(find_coordinates("right_image.jpg", "stam.txt"))
print(find_coordinates("left_image.jpg", "stam2.txt"))
print(match_stars("right_image.jpg", "left_image.jpg", "stam3.txt"))
