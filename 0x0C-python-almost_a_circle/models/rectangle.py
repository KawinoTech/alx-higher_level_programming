#!/usr/bin/python3
"""
...
"""


from base import Base


class Rectangle(Base):
    """
    ...
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        ...
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
        ...
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        ...
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
        ...
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        ...
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
        ...
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        ...
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
        ...
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        ...
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
        ...
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
        ...
        """
        return self.__width * self.__height

    def display(self):
        """
        ...
        """
        for i in range(self.__height):
            print(self.__width * '#', end="")
            print('\n', end='')

    def __str__(self):
        """
        ...
        """

        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            type(self).__name__, self.id, self.__x, self.__y,
            self.__width, self.__height)

    def update(self, *args):
        """
        ...
        """
        attrs = ['id', 'width', 'height', 'x', 'y']
        for i in range(len(args)):
            setattr(self, attrs[i], args[i])
