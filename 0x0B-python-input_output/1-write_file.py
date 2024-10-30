#!/usr/bin/python3
"""Contains a function write_file"""


def write_file(filename="", text=""):
    """
    Function that writes content into a file
    overwriting the existing content

    Args:
        filename: name of the file to be read
        text: content to be written
    Returns:
        no. of characters added
    """
    with open(filename, 'w', encoding="UTF-8") as f:
        f.write(text)
    return len(text)
