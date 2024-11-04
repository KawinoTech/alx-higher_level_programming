#!/usr/bin/python3
"""
Module containing Base class
Base class will be the “base” of all other classes in this project
"""
from base import Base


class Rectangle(Base):
    """
    Class Rectangle. inherits from class Base

    Attrs:
        private instance width: width of rectangle
        private instance height: width of height
        private instance x: x
        private instance y: y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        try:
            Rectangle.validator('width', width)
            Rectangle.validator('height', height)
            Rectangle.validator('x', x)
            Rectangle.validator('y', y)
        except Exception:
            raise
        else:
            self.__width = width
            self.__height = height
            self.__x = x
            self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        try:
            self.validator('width', value)
        except Exception:
            raise
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        try:
            self.validator('height', value)
        except Exception:
            raise
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        try:
            self.validator('x', value)
        except Exception:
            raise
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        try:
            self.validator('y', value)
        except Exception:
            raise
        else:
            self.__y = value

    @staticmethod
    def validator(name, value):
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
        else:
            if name == 'x' or name == 'y':
                if value < 0:
                    raise ValueError(f"{name} must be >= 0")
            if name == 'width' or name == 'height':
                if value <= 0:
                    raise ValueError(f"{name} must be > 0")

    def area(self):
        """Returns area of an instance"""
        return self.__width * self.__height

    def display(self):
        for i in range(self.__height):
            print(self.__width * '#', end="")
            print('\n', end='')

    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args):
        attrs = ['id', 'width', 'height', 'x', 'y']
        for i in range(len(args)):
            setattr(self, attrs[i], args[i])
