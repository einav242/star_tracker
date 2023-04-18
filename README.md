# star_tracker


## Overview

This code is a Python implementation of a program that detects stars in two images and matches them based on their coordinates.
This project uses the Hungarian algorithm.

## Requirements
This code requires the following Python packages:
- scipy
- numpy
- opencv-python

These can be installed using pip or any other package manager.

## Usage
The program contains two functions:
1. `find_coordinates(img_path, output_path=None)`: This function takes an image file path as input and returns a list of tuples containing the x and y coordinates, radius, and brightness of each star detected in the image. If an output file path is provided, it will also save the results to a text file with each tuple on a new line in the format "x,y,radius,brightness".
2. `find_matching_stars(img1_path, img2_path, output_path=None)`: This function takes two image file paths as input and returns a list of tuples containing pairs of matching stars between the two images. If an output file path is provided, it will also save the results to a text file with each tuple on a new line.

To use the code, simply run the Python script and call the desired function with the appropriate input parameters.

## Sample Data
The sample data consists of multy images of the night sky named "IMG_3046.jpg - IMG_3062.jpg". These images are included in the data directory and can be used to test the functionality of the program.

## Notes
 The library we built can only work with images of type JPG.

## Exampel

In the following image, the result of using the algorithm we wrote is shown. On the right side, you can see a text file where each line contains 2 numbers. The left number represents the ID of a star from the left image, and the right number represents the ID of a star from the right image that corresponds to the left star. It can be seen that all the stars that have a match are colored in green with their corresponding ID written, and all other stars are colored in a pale color.
![צילום מסך 2023-04-18 134843](https://user-images.githubusercontent.com/93386470/232755214-0675934c-3199-496a-a28f-86f842f84d52.png)

### By: Einav Benito -207051707, Shani ichai 318994183
