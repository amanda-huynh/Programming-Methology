#!/usr/bin/env python3

"""
  Stanford CS106A flights Project
"""

import sys


def parse_flights(text):
    """
    Given text that contain lines of flight data for
    different cities, return a list of flight data
    with the name and flight data for each city.
    >>> parse_flights('sfo,1,2\\nsfo,3,4\\n')
    {'sfo': [(1, 2), (3, 4)]}
    >>> parse_flights('sjc,2,5\\nsjc,4,6\\njfk,1,2\\nlax,1,3')
    {'sjc': [(2, 5), (4, 6)], 'jfk': [(1, 2)], 'lax': [(1, 3)]}
    >>> parse_flights('oak,1,3\\nmry,2,3\\nrdd,1,4\\npsp,1,2')
    {'oak': [(1, 3)], 'mry': [(2, 3)], 'rdd': [(1, 4)], 'psp': [(1, 2)]}
    """
    flights = {}
    lines = text.splitlines()
    for line in lines:
        data = line.split(',')
        city = data[0]
        if city not in flights:
            flights[city] = []
        num_flights = (int(data[1]), int(data[2]))  # convert the flight data pairs into ints
        flights[city].append(num_flights)
    return flights


def read_sched(filename):
    """
    (provided)
    Returns flights dict parsed from file.
    """
    with open(filename, 'r') as f:
        text = f.read()
    return parse_flights(text)


def main():
    # (provided)
    args = sys.argv[1:]
    flights = read_sched(args[0])
    print(flights)


if __name__ == '__main__':
    main()
