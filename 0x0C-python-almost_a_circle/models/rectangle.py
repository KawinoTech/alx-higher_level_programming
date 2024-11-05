#!/usr/bin/python3
"""
Module containing Rectangle class. Sub-class of Base
"""


from base import Base


class Rectangle(Base):
    """
    Class Rectangle. subclass of Base

    Attrs:
        private instance width: width of rectangle
        private instance height: width of height
        private instance x: x
        private instance y: y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize instance attributes.
        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X position of the rectangle.
            y (int): Y position of the rectangle.
            id (int): ID of the instance.
        """
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
        """
        Get width.
        Returns:
            width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set width
        Args:
            value (int): value
        """
        try:
            self.validator('width', value)
        except Exception:
            raise
        else:
            self.__width = value

    @property
    def height(self):
        """
        Get height
        Returns:
            height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set height
        Args:
            value (int): value
        """
        try:
            self.validator('height', value)
        except Exception:
            raise
        else:
            self.__height = value

    @property
    def x(self):
        """
        Get x
        Returns:
            x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set x
        Args:
            value (int): value
        """
        try:
            self.validator('x', value)
        except Exception:
            raise
        else:
            self.__x = value

    @property
    def y(self):
        """
        Get y
        Returns:
            y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set y
        Args:
            value (int): value
        """
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
            name (str): string
            value (int): value to be validated
        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `x` or `y` is less than 0.
            ValueError: If `width` or `height` is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        else:
            if name == 'x' or name == 'y':
                if value < 0:
                    raise ValueError(f"{name} must be >= 0")
            if name == 'width' or name == 'height':
                if value <= 0:
                    raise ValueError(f"{name} must be > 0")

    def area(self):
        """
        Find area of rectangle
        Returns:
            area of rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Displays a representation of a rectangle
        using '#'
        """
        for i in range(self.__height):
            print(self.__width * '#', end="")
            print('\n', end='')

    def __str__(self):
        """
        Returns the object representation of
        an instance
        """

        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            type(self).__name__, self.id, self.__x, self.__y,
            self.__width, self.__height)

    def update(self, *args):
        """
        Updates instance attributes.

        Args:
            *args (int): varying number of arguments
        """
        attrs = ['id', 'width', 'height', 'x', 'y']
        for i in range(len(args)):
            setattr(self, attrs[i], args[i])
