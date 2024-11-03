#!/usr/bin/python3
"""
Module that defines class BaseGeometry
"""


class BaseGeometry:
    """
    Class BaseGeometry
    """

    def area(self):
        """
        Raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates user input

        Args:
            name: string
            value: value to be validated
        Raises:
            TypeError: value is not an integer
            ValueError: value is less or equal to 0:
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
