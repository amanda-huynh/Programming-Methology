#!/usr/bin/env python3

"""
Stanford CS106A Crypto Project
"""

import sys

# provided ALPHABET constant - list of the regular alphabet
# in lowercase. Refer to this simply as ALPHABET in your code.
# This list should not be modified.
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def key_slug(key):
    """
    Given a key string, return the len-26 slug list for it.
    >>> key_slug('z')
    ['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    >>> key_slug('Bananas!')
    ['b', 'a', 'n', 's', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    >>> key_slug('Life, Liberty, and')
    ['l', 'i', 'f', 'e', 'b', 'r', 't', 'y', 'a', 'n', 'd', 'c', 'g', 'h', 'j', 'k', 'm', 'o', 'p', 'q', 's', 'u', 'v', 'w', 'x', 'z']
    >>> key_slug('Zounds!')
    ['z', 'o', 'u', 'n', 'd', 's', 'a', 'b', 'c', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'p', 'q', 'r', 't', 'v', 'w', 'x', 'y']
    """
    lowercase_key = key.lower()
    result = []
    copy_alphabet = list(ALPHABET) #make copy of alphabet
    for i in range(len(lowercase_key)):
        # return a char if it is not already in result and it is a letter, then remove every other instance of
        # the char from the copy of the alphabet
        if not lowercase_key[i] in result and lowercase_key[i].isalpha():
            result += lowercase_key[i]
            copy_alphabet.remove(lowercase_key[i])
    result += copy_alphabet
    return result


def encrypt_char(source, slug, char):
    """
    Given source and slug lists,
    if char is in source return
    its encrypted form, otherwise
    return it unchanged.
    # Using 'z' slug for testing.
    # Can set a var within a Doctest like this.
    >>> slug = ['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    >>> encrypt_char(ALPHABET, slug, 'A')
    'Z'
    >>> encrypt_char(ALPHABET, slug, 'n')
    'm'
    >>> encrypt_char(ALPHABET, slug, 'd')
    'c'
    >>> encrypt_char(ALPHABET, slug, '.')
    '.'
    >>> encrypt_char(ALPHABET, slug, '\\n')
    '\\n'
    """
    lowercase_char = char.lower()
    # if char is in key, look for the char at the same index in key and return an
    # upper/lower case encrypted char based on input char
    if lowercase_char in source:
        i = source.index(lowercase_char)
        result = slug[i]
        if char.isupper():
            return result.upper()
        return result
    return char


def encrypt_str(source, slug, s):
    """
    Given source and slug lists and string s,
    return a version of s where every char
    has been encrypted by source/slug.
    >>> slug = ['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    >>> encrypt_str(ALPHABET, slug, 'And like a thunderbolt he falls.\\n')
    'Zmc khjd z sgtmcdqanks gd ezkkr.\\n'
    """
    result = ''
    # encrypt each character in the string and return the encrypted string
    for ch in s:
        encrypted = encrypt_char(source, slug, ch)
        result += encrypted
    return result


def decrypt_str(source, slug, s):
    """
    Given source and slug lists, and encrypted string s,
    return the decrypted form of s.
    >>> slug = ['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    >>> decrypt_str(ALPHABET, slug, 'Zmc khjd z sgtmcdqanks gd ezkkr.\\n')
    'And like a thunderbolt he falls.\\n'
    """
    # switching parameters from encrypt_str to decrypt the string
    return encrypt_str(slug, source, s)


def encrypt_file(filename, key):
    """
    Given filename and key, compute and
    print the encrypted form of its lines.
    """
    # opening file and setting everything to f and running through each line to encrypt
    with open(filename, 'r') as f:
        for line in f:
            print(encrypt_str(ALPHABET, key_slug(key), line))


def decrypt_file(filename, key):
    """
    Given filename and key, compute and
    print the decrypted form of its lines.
    """
    # opening file and setting everything into f and running through each line to decrypt
    with open(filename, 'r') as f:
        for line in f:
            print(decrypt_str(ALPHABET, key_slug(key), line))


def main():
    """
    Encrypt or decrypt files when commands are given to do so in the command line 
    """
    args = sys.argv[1:]
    # 2 command line argument patterns:
    # -encrypt key filename
    # -decrypt key filename
    # Call encrypt_file() or decrypt_file() based on the args.
    filename = args[2]
    key = args[1]
    # the length of the argument in the command line is 3 and the argument is to encrypt/decrypt
    # file, encrypt/decrypt file
    if len(args) == 3 and args[0] == '-encrypt':
        encrypt_file(filename, key)
    if len(args) == 3 and args[0] == '-decrypt':
         decrypt_file(filename, key)



# Python boilerplate.
if __name__ == '__main__':
    main()
