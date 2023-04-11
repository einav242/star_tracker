# star_tracker


## Overview
This code is a Python implementation of a program that detects stars in two images and matches them based on their coordinates. 

## Requirements
This code requires the following Python packages:
- skimage
- numpy
- opencv-python

These can be installed using pip or any other package manager.

## Usage
The program contains two functions:
1. `find_coordinates(img_path, output_path=None)`: This function takes an image file path as input and returns a list of tuples containing the x and y coordinates, radius, and brightness of each star detected in the image. If an output file path is provided, it will also save the results to a text file with each tuple on a new line in the format "x,y,radius,brightness".
2. `match_stars(img1_path, img2_path, output_path=None)`: This function takes two image file paths as input and returns a list of tuples containing pairs of matching stars between the two images. If an output file path is provided, it will also save the results to a text file with each tuple on a new line.

To use the code, simply run the Python script and call the desired function with the appropriate input parameters. The sample code at the end of the script demonstrates how to use both functions.

## Sample Data
The sample data consists of two images of the night sky named "right_image.jpg" and "left_image.jpg". These images are included in the same directory as the Python script and can be used to test the functionality of the program.

## Notes
- The `distance()` function calculates the Euclidean distance between two points in a two-dimensional space.
- The `blob_log()` function from the skimage package is used to detect stars in the images.
