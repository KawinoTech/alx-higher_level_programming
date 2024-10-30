#!/usr/bin/python3
"""Contains a function from_json_string"""


import json


def from_json_string(my_str):
    """
     function that returns an object (Python data structure)
     represented by a JSON string

    Args:
        my_str: object to be loaded into python object
    Returns:
        python data structure of my_str
    """
    return json.loads(my_str)
