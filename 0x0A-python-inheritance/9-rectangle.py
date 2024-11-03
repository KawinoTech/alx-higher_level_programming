#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle, subclass of BaseGeometry

    Attrs:
        width: width of the rectangle
        height: height of the rectangle
    """
    def __init__(self, width, height):
        try:
            super().integer_validator('width', width)
            super().integer_validator('height', height)
        except Exception:
            raise
        else:
            self.__width = width
            self.__height = height

    def __str__(self):
        """
        Returns string representation of an object
        """
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"

    def __ptr__(self):
        """
        Prints string representation of an object
        """
        print(f"[{self.__class__.__name__}] {self.__width}/{self.__height}")

    def area(self):
        return self.__width * self.__height
