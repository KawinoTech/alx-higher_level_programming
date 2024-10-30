#!/usr/bin/python3
"""Contains a function write_file"""


def append_write(filename="", text=""):
    """
    Function that appends content into a file
    does not overwriting the existing content

    Args:
        filename: name of the file to be read
        text: content to be written
    Returns:
        NULL
    """
    with open(filename, 'a', encoding="UTF-8") as f:
        f.write(text)
    return len(text)
