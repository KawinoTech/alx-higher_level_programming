#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square, subclass of Rectangle
    """

    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """square area"""
        return self.__size**2

    def __str__(self):
        """
        Returns string representation of an object
        """
        return f"[{self.__class__.__name__}] {self.__size}/{self.__size}"

    def __ptr__(self):
        """
        Prints string representation of an object
        """
        print(f"[{self.__class__.__name__}] {self.__size}/{self.__size}")
