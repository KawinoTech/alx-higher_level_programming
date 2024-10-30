#!/usr/bin/python3
"""Contains a function read_file"""


def read_file(filename=""):
    """
    Function that reads a text file (UTF8) and prints it to stdout

    Args:
        filename: name of the file to be read
    Returns:
        NULL
    """
    with open(filename, 'r', encoding="UTF-8") as f:
        print(f.read())
