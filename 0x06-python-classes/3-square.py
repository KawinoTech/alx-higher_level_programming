#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Defines blueprint for square objects"""
    def __init__(self, size=0):
        """
        Args:
            size (str): size of square.
        Raises:
                TypeError: if size is not an integer
                ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the area of the square object"""
        return self.__size**2
