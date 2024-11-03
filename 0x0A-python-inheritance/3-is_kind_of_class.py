#!/usr/bin/python3
"""
Module containing function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    Function that returns True if the object is exactly an
    instance of the specified class, or a subclass of
    the specified class
    Args:
        obj: object to be tested
        a-class: class name reference point
    """
    if isinstance(obj.__class__.__name__, a_class):
        return True
    if issubclass(obj.__class__, a_class):
        return True
    return False
