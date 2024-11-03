#!/usr/bin/python3
"""
Module that defines Recctangle
"""


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
