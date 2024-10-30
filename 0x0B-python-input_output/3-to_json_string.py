#!/usr/bin/python3
"""Contains a function to_json_string"""


import json


def to_json_string(my_obj):
    """
    Function that returns the JSON representation of an object (string)

    Args:
        my_obj: object to be dumped into json string
    Returns:
        json string of my_obj
    """
    return json.dumps(my_obj)
