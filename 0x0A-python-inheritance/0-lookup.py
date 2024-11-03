#!/usr/bin/python3
"""
Module containing function look_up
"""


def lookup(obj):
    """
    Function that returns the list of available
    attributes and methods of an object

    Args:
        obj:  Object source
    """
    return obj.__dir__()
