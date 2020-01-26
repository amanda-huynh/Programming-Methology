#!/usr/bin/env python3

"""
Stanford CS106A Quilt Project
"""

import sys
from drawcanvas import DrawCanvas


def draw_bars(canvas, x, y, width, height, n):
    """
    Draw bars in the given canvas at x, y, with width, height, n
    """
    canvas.draw_rect(x, y, width, height, color='lightblue')
    for i in range(n):
        x_add = (i / (n - 1)) * (width - 1)
        canvas.draw_line(x + x_add, y, x + x_add - 1, y + height - 1, color='black')  # FR: maybe just x + x_add


def draw_eye(canvas, x, y, width, height, n):
    """
    Draw eye in the given canvas at x, y, with width, height, n
    """
    canvas.draw_rect(x, y, width, height, color='lightblue')
    canvas.fill_oval(x, y, width, height, color='yellow')
    for i in range(n):
        x_add = (i / (n - 1)) * (width - 1)
        canvas.draw_line(x + width // 2, y + height // 2, x + x_add, y + height - 1, color='black')

def draw_bowtie(canvas, x, y, width, height, n):
    """
    Draw bowtie in the given canvas at x, y, with width, height, n
    """

    canvas.draw_rect(x, y, width, height, color='lightblue')
    for i in range(n):
        y_add = (i / (n - 1)) * (height - 1)
        canvas.draw_line(x, y + y_add, x + width - 1, y + (height - 1) - y_add, color='red')   # FR: can also switch x1 and y1

def draw_quilt(width, height, n):
    """
    Create a canvas of width, height and draw the whole
    quilt on it. Draw a n-by-n grid of patches.
    """
    canvas = DrawCanvas(width, height, fast_draw=True, title="Quilt")
    sub_width = width // n
    sub_height = height // n
    for row in range(n):
        for col in range(n):
            x = col * sub_width
            y = row * sub_height
            canvas.draw_rect(x, y, sub_width, sub_height, color='lightblue')
            choice = (row + col) % 3
            if choice == 0:
                draw_bars(canvas, x, y, sub_width, sub_height, n)
            if choice == 1:
                draw_bowtie(canvas, x, y, sub_width, sub_height, n)
            if choice == 2:
                draw_eye(canvas, x, y, sub_width, sub_height, n)

# main() code is complete.
# There are 5 command lines that work here,
# with width/height/n being positive integers.
#  -bars width height n
#  -eye width height n
#  -bowtie width height n
#  -quilt width height n
# e.g. run like this in the terminal:
#  python3 quilt.py -bars 600 400 10


def main():
    # Standard first line of main to get args
    args = sys.argv[1:]

    if len(args) != 4:
        print('usage: (one of -bars, -eye, -bowtie, -draw_quilt) width height n')
        return

    # Parse width/height/n from command line, giving a helpful
    # error message if it fails.
    try :
        width = int(args[1])
        height = int(args[2])
        n = int(args[3])
    except Exception as e:
        print("Error parsing int width/height/n from command line:" + ' '.join(args))
        return

    # Tricky: we do all the drawing in a try, so that if it takes an exception,
    # we can still do the mainloop() at the end. If we do not do this, an exception
    # causes no graphics output to appear which makes debugging hard.
    try:
        if args[0] == '-bars':
            canvas = DrawCanvas(width * 2, height * 2, fast_draw=True, title='Quilt')
            # Can change to fast_draw=False .. drawing plays out more slowly
            draw_bars(canvas, 0, 0, width, height, n)
            draw_bars(canvas, width, height, width, height, n)

        if args[0] == '-eye':
            canvas = DrawCanvas(width * 2, height * 2, fast_draw=True, title='Quilt')
            draw_eye(canvas, 0, 0, width, height, n)
            draw_eye(canvas, width, height, width, height, n)

        if args[0] == '-bowtie':
            canvas = DrawCanvas(width * 2, height * 2, fast_draw=True, title='Quilt')
            draw_bowtie(canvas, 0, 0, width, height, n)
            draw_bowtie(canvas, width, height, width, height, n)

        if args[0] == '-quilt':
            draw_quilt(width, height, n)

    # Print out exception from draw
    except Exception as e:
        print(e)

    DrawCanvas.mainloop()


if __name__ == '__main__':
    main()
