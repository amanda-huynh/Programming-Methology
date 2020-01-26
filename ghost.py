#!/usr/bin/env python3

"""
Stanford CS106A Ghost Project
"""

import os
import sys
import math

# This line imports SimpleImage for use here
# This depends on the Pillow package
from simpleimage import SimpleImage


def pix_dist2(pix1, pix2):
    """
    Returns the square of the color distance between 2 pix tuples.
    >>> pix_dist2((5, 5, 5), (27, 27, 27))
    38.1051177665153
    >>> pix_dist2((4, 2, 1), (20, 5, 6))
    17.029386365926403
    >>> pix_dist2((40, 22, 11), (30, 15, 18))
    14.071247279470288
    """
    x_difference = pix2[0] - pix1[0]    # taking the difference of each RGB in pix tuples
    y_difference = pix2[1] - pix1[1]
    z_difference = pix2[2] - pix1[2]

    return math.sqrt(x_difference ** 2 + y_difference ** 2 + z_difference ** 2)


def average_RGB(pixs):
    """
    Given a list of 3 or more pix, compute the
    average RGB for each pix in the list of RGB tuples.
    """
    r_sum = 0
    g_sum = 0
    b_sum = 0
    for pix in pixs:
        r_sum += pix[0]  # add up each RGB in every RGB tuple in the list of RGB tuples
        g_sum += pix[1]
        b_sum += pix[2]
    average = (r_sum / len(pixs), g_sum / len(pixs), b_sum / len(pixs))  # put avg val of each RGB into a tup
    return average

def best_pix(pixs):
    """
    Given a list of 3 or more pix, returns the best pix.
    >>> best_pix([(1, 10, 13), (23, 11, 9), (28, 28, 28)])
    (23, 11, 9)
    >>> best_pix([(2, 4, 6,), (3, 2, 7), (30, 20, 1)])
    (2, 4, 6)
    >>> best_pix([(20, 34, 15,), (23, 8, 71), (5, 21, 10)])
    (20, 34, 15)
    """
    return min(pixs, key = lambda pix: pix_dist2(average_RGB(pixs), pix)) # return min distance between avg and each pix


def solve(images):
    """
    Given a list of image objects, compute and show
    a Ghost solution image based on these images.
    There will be at least 3 images and they will all be
    the same size.
    """

    image = images[0]
    solution = SimpleImage.blank(image.width, image.height)
    for y in range(image.height):
        for x in range(image.width):
            pix_list = []
            for image in images:
                pix = image.get_pix(x, y)
                pix_list.append(pix)

            img_pix = best_pix(pix_list)  # best pix in the at least 3 images

            solution.set_pix(x, y, img_pix) # set pix from best RGB tuple to the solution img
    solution.show()


def jpgs_in_dir(dir):
    """
    (provided)
    Given the name of a directory
    returns a list of the .jpg filenames within it.
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided)
    Given a directory name, reads all the .jpg files
    within it into memory and returns them in a list.
    Prints the filenames out as it goes.
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print(filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    if len(args) == 1:
        images = load_images(args[0])
        solve(images)


if __name__ == '__main__':
    main()
