#!/usr/bin/python3

"""Contains class rectangle"""
class Rectangle:
    """Defines class rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        int: instance property size getter
        @width.setter: instance property size getter
                    Raises:
                        TypeError: if width is not an integer
                        ValueError: if width is less than 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    @property
    def height(self):
        """
        int: instance property size getter
        @height.setter: instance property size getter
                    Raises:
                        TypeError: if height is not an integer
                        ValueError: if height is less than 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            return "{:s}\n".format(Rectangle.print_symbol * self.__width) * self.__height
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1 == rect_2:
            return rect_1
        return max(rect_1.area(), rect_2.area())
    @classmethod
    def square(cls, size=0):
        return cls(size, size)
