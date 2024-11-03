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
            self.integer_validator('width', width)
            self.integer_validator('height', height)
        except Exception:
            raise
        else:
            self.__width = width
            self.__height = height
