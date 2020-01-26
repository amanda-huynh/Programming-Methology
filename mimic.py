#!/usr/bin/env python3

import random
import sys

"""
Stanford CS106A Mimic Project.
"""


def bigrams(bigrams_data, entire_text):
    """
    Given full string of text from filename, build dict of
    word strings and every word afterwards and return it.
    >>> bigrams({}, 'Whenever there is here and. me there you questions; and whenever')
    {'': ['Whenever'], 'Whenever': ['there'], 'there': ['is', 'you'], 'is': ['here'], 'here': ['and.'], 'and.': ['me'], 'me': ['there'], 'you': ['questions;'], 'questions;': ['and'], 'and': ['whenever']}
    >>> bigrams({}, 'Hello and there but and gorgeous rocks hi.')
    {'': ['Hello'], 'Hello': ['and'], 'and': ['there', 'gorgeous'], 'there': ['but'], 'but': ['and'], 'gorgeous': ['rocks'], 'rocks': ['hi.']}
    >>> bigrams({}, 'Mood her him their us. we')
    {'': ['Mood'], 'Mood': ['her'], 'her': ['him'], 'him': ['their'], 'their': ['us.'], 'us.': ['we']}
    """
    words = entire_text.split()
    bigrams_data[''] = [words[0]] # empty string case
    for i in range(len(words) - 1):
        if words[i] not in bigrams_data:
            bigrams_data[words[i]] = []
        bigrams_data[words[i]].append(words[i + 1]) # map each word to the next word
    return bigrams_data


def run_bigrams_printout(bigrams, minimum):
    """
    Given bigrams dict and min num, print previous word with a space afterwards
    until the min number is reached. When min is reached, stop printing at the next
    word that ends with'.' or ';'.
    """
    count = 0
    previous = ''
    while True:
        previous = word_output(bigrams, previous).strip()
        print(previous, end=' ')
        count += 1

        if count >= minimum and (previous.endswith('.') or previous.endswith(';')):
            print('')
            break


def word_output(bigrams, current_word):
    """
    Given bigrams dict and current word, randomly generate the output
    value for each key.
    """
    if current_word not in bigrams:
        values = bigrams['']
    else:
        values = bigrams[current_word]
    return random.choice(values)


def read_file(filename):
    """
    Given filename, read file and build and return a bigrams dict.
    """
    data = {}
    with open(filename, 'r') as f:
        text = f.read() + ' ' # compiling every line from filename into new var
        bigrams_dict = bigrams(data, text)
    return bigrams_dict


def main():
    args = sys.argv[1:]
    minimum = 25  # default minimum value
    bigrams_dict = read_file(args[0])   # create data dict
    if len(args) == 1:  # default min
        run_bigrams_printout(bigrams_dict, minimum)

    if len(args) == 2:  # custom min
        minimum = int(args[1])
        run_bigrams_printout(bigrams_dict, minimum)






if __name__ == '__main__':
    main()

