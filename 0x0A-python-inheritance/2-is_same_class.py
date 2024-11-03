#!/usr/bin/python3
"""
Module containing function is_same_class
"""


def is_same_class(obj, a_class):
    """
    Function that returns True if the object is exactly an
    instance of the specified class
    Args:
        obj: object to be tested
        a-class: class name reference point
    """
    return True if type(obj) is a_class else False
