#!/usr/bin/env python3

"""
Stanford CS106A BabyGraphics GUI
built on babynames data
"""

import sys
import tkinter
import babynames


def make_gui(top, width, height, names):
    """
    (provided)
    Set up the GUI elements for Baby Names, returning the TK Canvas to use.
    top is TK root, width/height is canvas size, names is BabyNames dict.
    """
    # name entry field
    entry = tkinter.Entry(top, width=60, name='entry', borderwidth=2)
    entry.grid(row=0, columnspan=12, sticky='w')
    entry.focus()

    # canvas for drawing
    canvas = tkinter.Canvas(top, width=width, height=height, name='canvas')
    canvas.grid(row=1, columnspan=12, sticky='w')

    space = tkinter.LabelFrame(top, width=10, height=10, borderwidth=0)
    space.grid(row=2, columnspan=12, sticky='w')

    # Search field etc. at the bottom
    label = tkinter.Label(top, text='Search:')
    label.grid(row=3, column=0, sticky='w')
    search_entry = tkinter.Entry(top, width=15, name='searchentry')
    search_entry.grid(row=3, column=1, sticky='w')
    search_out = tkinter.Text(top, height=3, width=70, name='searchout', borderwidth=2)
    search_out.grid(row=3, column=3, sticky='w')

    # When <return> key is hit in a text field .. connect to the handle_draw()
    # and handle_search() functions to do the work.
    entry.bind('<Return>', lambda event: handle_draw(entry, canvas, names))
    search_entry.bind('<Return>', lambda event: handle_search(search_entry, search_out, names))

    top.update()
    return canvas


def handle_draw(entry, canvas, names):
    """
    (provided)
    Called when <return> key hit in given text entry field.
    Gets search text, looks up names, calls draw_names()
    for those names to draw the results.
    """
    text = entry.get()
    lookups = text.split()
    draw_names(canvas, names, lookups)


def handle_search(search_entry, search_out, names):
    """
    (provided) Called for <return> key in lower search field.
    Calls babynames.search() and displays results in GUI.
    Gets search target from given search_entry, puts results
    in given search_out text area.
    """
    target = search_entry.get().strip()
    search_out.delete('1.0', tkinter.END)
    # GUI detail: by deleting always, but only putting in new text
    # if there is data .. hitting return on an empty field
    # lets the user clear the output.
    if target:
        # Call the search_names function in babynames.py
        result = babynames.search_names(names, target)
        out = ' '.join(result)
        #searchout = top.children['searchout']  # alt strategy to access fields
        search_out.insert('1.0', out)


# Provided constants to load and draw the baby data
FILENAMES = ['baby-1900.txt', 'baby-1910.txt', 'baby-1920.txt', 'baby-1930.txt',
             'baby-1940.txt', 'baby-1950.txt', 'baby-1960.txt', 'baby-1970.txt',
             'baby-1980.txt', 'baby-1990.txt', 'baby-2000.txt', 'baby-2010.txt']
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
SPACE = 20
COLORS = ['lightblue', 'purple', 'green', 'blue']  # changed to light blue because I can't see red
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def year_index_x(width, year_index):
    """
    Given canvas width and year_index 0, 1, 2 .. into YEARS list,
    return the x value for the vertical line for that year.
    """
    x_val = SPACE + year_index * (width - (2 * SPACE)) / len(YEARS)
    return x_val


def draw_fixed(canvas):
    """
    Erases the given canvas and draws the fixed lines on it.
    """
    canvas.delete('all')
    width = canvas.winfo_width()
    height = canvas.winfo_height()

    canvas.create_line(SPACE, SPACE, width - SPACE, SPACE)  # top horizontal line
    canvas.create_line(SPACE, height - SPACE, width - SPACE, height - SPACE)    # bottom horizontal line

    for i in range(len(YEARS)): # vertical lines for each year
        y1 = 0
        y2 = height
        x1 = year_index_x(width, i)

        canvas.create_line(x1, y1, x1, y2)
        canvas.create_text(x1, y2 - SPACE, text=YEARS[i], anchor=tkinter.NW)    # labeling each year in x axis


def draw_names(canvas, names, lookups):
    """
    Given canvas, names dict, lookups list of name strs,
    Draw the data for the lookups on the canvas.
    """
    draw_fixed(canvas)
    width = canvas.winfo_width()
    height = canvas.winfo_height()

    for name_index in range(len(lookups)):  # for each person
        name = lookups[name_index]
        previous_x = 0
        previous_y = 0
        for i in range(len(YEARS)):  # each line, label for each person
            x1 = year_index_x(width, i)
            if YEARS[i] in names[name]:
                rank = names[name][YEARS[i]]
            else:
                rank = MAX_RANK

            y1 = (height - (2 * SPACE)) / (MAX_RANK - 1) * (rank - 1) + SPACE   # diff y values for name each year

            color_num = name_index % len(COLORS)  # after all 4 colors, wrap around and use 1st color again

            if i > 0:
                canvas.create_line(x1, y1, previous_x, previous_y, width = 2, fill = COLORS[color_num])
            canvas.create_text(x1, y1, text=(name, rank), anchor=tkinter.SW, fill = COLORS[color_num])

            previous_x = x1 # remember previous x, y values
            previous_y = y1







# main() code is provided
def main():
    args = sys.argv[1:]
    # Establish size - user can override
    width = 1000
    height = 600
    # Let command line override size of window
    if len(args) == 2:
        width = int(args[0])
        height = int(args[1])

    # Load data
    names = babynames.read_files(FILENAMES)

    # Make window
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = make_gui(top, width, height, names)

    # draw_fixed once at startup so we have the lines
    # even before the user types anything.
    draw_fixed(canvas)

    # This needs to be called just once
    top.mainloop()


if __name__ == '__main__':
    main()
