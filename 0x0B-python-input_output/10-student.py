#!/usr/bin/python3
"""
This is the "Student"  module.

This module provides a Student class.
"""


class Student:
    """A Student class with attributes first_name, last_name and age,
    methods to_json
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        """
        dict_1 = {}

        if attrs != None:
            for i in range(len(attrs)):
                try:
                    dict_1[attrs[i]] = getattr(self, attrs[i])
                except AttributeError:
                    continue
            return dict_1
        else:
            return vars(self)
