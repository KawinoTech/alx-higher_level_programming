#!/usr/bin/python3
"""Contains a function save_to_json_file"""


import json


def load_from_json_file(filename):
    """
     Function that creates an Object from a “JSON file”

    Args:
        filename: file where json string will be loaded
    Returns:
        NULL
    """
    with open(filename, 'r', encoding="UTF-8") as f:
        obj = json.load(f)
    return obj
