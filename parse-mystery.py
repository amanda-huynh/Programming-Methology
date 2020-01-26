#!/usr/bin/env python3

"""
Stanford CS106A Parse Mystery Project
"""

import sys

# Next line depends on Pillow package
from simpleimage import SimpleImage

def parse_line(s):
    """
    Given a string s, parse the ints out of it and
    return them as a list of int values.
    # 3 tiny cases provided to start
    >>> parse_line('1')
    [1]
    >>> parse_line('1$')
    [1]
    >>> parse_line('12$')
    [21]
    >>> parse_line('800!)176^b006$(46$*#63Z*16$*06$z5^')
    [800, 600, 64, 63, 61, 60]
    >>> parse_line('1334')
    [1334]
    >>> parse_line('32552$')
    [25523]
    >>> parse_line('019183^')
    []
    """
    search = 0
    numbers = []
    reverse = ''
    while True:
        begin = search
        # search through string s until the first occurrence of a digit
        while begin < len(s) and not s[begin].isdigit():
            begin += 1

        if begin > len(s):
            break

        if s.isdigit():
            numbers.append(int(s))

        end = begin + 1
        while end < len(s) and s[end].isdigit():
            end += 1
        nums = s[begin:end]

        # reverse string if there is a '$'
        if end < len(s) and s[end] == '$':
            for ch in nums:
                reverse = ch + reverse
            numbers.append(int(reverse))

        # omits numbers if there is a '^'
        elif end < len(s) and s[end] != '^':
            numbers.append(int(nums))

        reverse = ''
        search = end + 1
    return numbers


def parse_file(filename):
    """
    Given filename, parse out and return a list of all that file's
    int values.
    (test provided)
    >>> parse_file('3lines.txt')
    [800, 600, 64, 63, 61, 60, 74, 81, 55, 56]
    """
    result = []
    with open(filename, 'r') as f:
        for line in f:
            result += parse_line(line)
    return result


def solve_mystery(filename):
    """Solve the mystery as described in the handout."""

    # SimpleImage boilerplate provided as a starting point

    parsing = parse_file(filename)

    width = parsing[0]
    height = parsing[1]

    start = 2 # where to begin looking at RGB colors in parsed list
    image = SimpleImage.blank(width, height)
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            pixel.red = parsing[start] # set red pixel to the first RGB color in the parsed list
            pixel.green = pixel.red # set all RGB colors to the same value for greyscale
            pixel.blue = pixel.red
            start += 1



    # This displays image on screen
    image.show()


def main():
    # (provided code)
    # Command lines:
    # 1. -nums file.txt -> prints numbers
    # 2. file.txt -> shows image solution
    args = sys.argv[1:]
    if len(args) == 2 and args[0] == '-nums':
        nums = parse_file(args[1])
        print(nums)
    if len(args) == 1:
        solve_mystery(args[0])


if __name__ == '__main__':
    main()
