#!/usr/bin/env python3

"""
Stanford CS106A Swizzler project
"""

import sys

# --define helper functions here--

def start(s):
    """
    Given string s, start from the beginning and look for the first occurrence
    of an alphabetic char. Slice from the beginning to i. If found, break out
    of the loop and return all non-alphabetical chars.
    >>> start('+==+Hello!!')
    '+==+'
    >>> start('^#@abaaa#%$')
    '^#@'
    >>> start('!!!!ayy@')
    '!!!!'
    >>> start('^#@abaaa#%$')
    '^#@'
    >>> start('')
    ''
    """
    result = ''
    for i in range(len(s)):
        if s[i].isalpha():
            result += s[:i]
            break
    return result


def end(s):
    """
    Given string s, start from the end of the string and look for the first
    occurrence of an alpha char. If found, break and return all non-alpha char
    after that first alpha.
    >>> end('+==+Hello!!')
    '!!'
    >>> end('^#@abaaa#%$')
    '#%$'
    >>> end('#$%%hiiiiiiiii!')
    '!'
    >>> end('%hello###')
    '###'
    >>> end('')
    ''
    """
    result = ''
    for i in range(len(s) - 1): #starting from end of string
        if s[len(s) - i - 1].isalpha():
            result += s[len(s) - i:] #all non-alpha char from the end of the string
            break
    return result


def swizzled_alpha(s):
    """
    For all alpha char between the first two alpha char and the last alpha
    char, reverse the order.
    >>> swizzled_alpha('Notebook')
    'oobet'
    >>> swizzled_alpha('Luxury')
    'rux'
    >>> swizzled_alpha('Animal')
    'ami'
    >>> swizzled_alpha('')
    ''
    """
    result = ''
    middle = s[2:len(s) - 1]
    # swizzle the middle if the string has 5 or more chars
    for ch in middle:
        if len(s) >= 5:
            result = ch + result
    return result


def swizzle(s):
    """
    Compute and return the swizzled version of string s.
    This is complicated, but can make heavy use of decomposed functions.
    No loops are required in this function.
    >>> swizzle('++Python!')
    '++Pyohtn!'
    >>> swizzle('^^^abcdefg$$$')
    '^^^abfedcg$$$'
    >>> swizzle('^ad-hoc$')
    '^adoh-c$'
    >>> swizzle('$^-@')  # 100% punctuation
    '$^-@'
    >>> swizzle('abcde')
    'abdce'
    >>> swizzle('abcd')
    'abcd'
    >>> swizzle('a')
    'a'
    >>> swizzle('')
    ''
    >>> swizzle('ab')
    'ab'
    >>> swizzle('abc')
    'abc'
    """
    result = ''
    # if empty string, return nothing
    if len(s) == 0:
        return ''
    # find first two alpha chars in string
    beginning_alpha = s[len(start(s)): len(start(s)) + 2]
    # find last alpha char in string
    last_alpha = s[len(s) - len(end(s)) - 1]
    # alpha chars after the first two alpha chars and before the
    # last alpha char in string
    middle = s[len(start(s)): len(s) - len(end(s))]
    if len(s) < 5:
        return s
    # put together the non-alpha chars, first two alpha chars in string,
    # the swizzled chars, the last alpha char, and non-alpha chars at the
    # end of the string
    result += start(s) + beginning_alpha + swizzled_alpha(middle) + last_alpha + end(s)
    return result



def swizzle_file(filename):
    """
    (provided code)
    Print out the contents of the given filename
    with each of its words swizzled.
    Works by splitting each line into "words",
    calling the swizzle() function to compute
    the swizzled version of each word for printing.
    """
    with open(filename, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                swizzled = swizzle(word)
                print(swizzled + ' ', end='')
            print()  # print '\n' at end of each line


def main():
    """
    (provided code)
    The 1 command line argument is the file to process.
    Calls swizzle_file() with this filename to print it out.
    """
    args = sys.argv[1:]
    if len(args) == 1:
        swizzle_file(args[0])


# Python boilerplate
if __name__ == '__main__':
    main()
