#!/usr/bin/python3
"""Contains a function save_to_json_file"""


import json


def save_to_json_file(my_obj, filename):
    """
     Function that writes an Object to a text file, using a JSON representation

    Args:
        my_obj: object to be dumped into json file
        format = json string
        filename: file where json string will be dumped
    Returns:
        NULL
    """

    with open(filename, 'w', encoding="UTF-8") as f:
        json.dump(my_obj, f)
