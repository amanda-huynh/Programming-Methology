#!/usr/bin/env python3

"""
Stanford CS106A BabyNames Project
Part-A : organizing the bulk data
"""

import sys


def add_name(names, year, rank, name):
    """
    Add the given data: int year, int rank, str name
    to the given names dict and return it.
    (1 test provided, more tests TBD)
    >>> add_name({}, 2000, 10, 'abe')
    {'abe': {2000: 10}}
    >>> add_name({}, 1951, 30, 'hellen')
    {'hellen': {1951: 30}}
    >>> add_name({}, 2010, 2, 'amanda')
    {'amanda': {2010: 2}}
    >>> add_name({}, 1500, 60, 'teresa')
    {'teresa': {1500: 60}}
    >>> add_name({}, 1999, 78, 'jacob')
    {'jacob': {1999: 78}}
    >>> add_name({'julia': {1751: 78}}, 2001, 88, 'julia')
    {'julia': {1751: 78, 2001: 88}}
    >>> add_name({'jose': {1920: 78}}, 1920, 20, 'jose')
    {'jose': {1920: 20}}
    """

    if name in names:
        data = names[name]  # giving us access to value of name
        if year in data and data[year] > rank:   # proceed if year exists in dict and value at year is greater than rank
            data[year] = rank   # within that dict, put in year as the key, set rank as value
        elif year not in data:
            data[year] = rank
    else:
        names[name] = {}    # if name not in dict, create an empty dict as val of key
        data = names[name]
        data[year] = rank
    return names


def add_file(names, filename):
    """
    Given a names dict and babydata.txt filename, add the file's data
    to the dict and return it.
    (Tests provided, Code TBD)
    >>> add_file({}, 'small-2000.txt')
    {'A': {2000: 1}, 'B': {2000: 1}, 'C': {2000: 2}}
    >>> add_file({}, 'small-2010.txt')
    {'C': {2010: 1}, 'D': {2010: 1}, 'A': {2010: 2}, 'E': {2010: 2}}
    >>> add_file({'A': {2000: 1}, 'B': {2000: 1}, 'C': {2000: 2}}, 'small-2010.txt')
    {'A': {2000: 1, 2010: 2}, 'B': {2000: 1}, 'C': {2000: 2, 2010: 1}, 'D': {2010: 1}, 'E': {2010: 2}}
    """
    with open(filename, 'r') as f:
        # read each line and cut out \n from each line
        reading = f.readline()
        cut = reading.strip()
        year = int(cut)

        for line in f:
            separate = line.split(',')
            rank = int(separate[0].strip())  # return a clean version of the rank and names without extra whitespace
            name = separate[1].strip()
            add_name(names, year, rank, name)  # returning first instance of name

            name = separate[2].strip()
            add_name(names, year, rank, name)   # returning other instances of name in dict after first instance
        return names

def read_files(filenames):
    """
    Given list of filenames, build and return a names dict
    of all their data.
    """
    names = {}
    for filename in filenames:
            add_file(names, filename)
    return names


def search_names(names, target):
    """
    Given names dict and a target string,
    return a sorted list of all the name strings
    that contain that target string anywhere.
    Not case sensitive.
    (Code and tests TBD)
    >>> names = {'collen': {}, 'hellen': {}, 'anna': {}}
    >>> search_names(names, 'll')
    ['collen', 'hellen']
    >>> names = {'Allen': {}, 'Aliyah': {}, 'ally': {}}
    >>> search_names(names, 'Al')
    ['Aliyah', 'Allen', 'ally']
    >>> names = {'brianna': {}, 'amanda': {}, 'Brock': {}}
    >>> search_names(names, 'Br')
    ['Brock', 'brianna']
    """
    new_names = []
    for name in names.keys():
        if len(name) > 0 and target.lower() in name.lower():    # account for range, and not case-sensitive case
            new_names.append(name)
    return sorted(new_names)


def print_names(names):
    """
    (provided)
    Given names dict, print out all its data, one name per line.
    The names are printed in increasing alphabetical order,
    with its years data also in increasing order, like:
    Aaden [(2010, 560)]
    Aaliyah [(2000, 211), (2010, 56)]
    ...
    Surprisingly, this can be done with 2 lines of code.
    We'll explore this in lecture.
    """
    for key, value in sorted(names.items()):
        print(key, sorted(value.items()))


def main():
    # (provided)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Change filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
