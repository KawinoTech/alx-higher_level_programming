#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Defines blueprint for square objects"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size (str): size of square.
        Raises:
                TypeError: if size is not an integer
                ValueError: if size is less than 0
                TypeError: if any element of tuple is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.__position = position

    def area(self):
        """Returns the area of the square object"""
        return self.__size**2

    @property
    def size(self):
        """
        int: instance property size getter
        @size.setter: instance property size getter
                    Raises:
                        TypeError: if size is not an integer
                        ValueError: if size is less than 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """prints in stdout the square with the character #

        prints the square using '#' characters
        also takes into account position (x, y) offsets
        """
        i = 0
        if self.__size == 0:
            print()
            return
        for i in range(0, self.__position[1]):
            print()
        i = 0
        for i in range(0, self.__size):
            j = 0
            x_pad = 0
            for x_pad in range(0, self.__position[0]):
                print(" ", end='')
            for j in range(0, self.__size):
                print("#", end='')
            print()
    @property
    def position(self):
        """
        tuple: instance property position getter
        @position.setter: instance property size getter
                    Raises:
                        TypeError: position must be a tuple of 2 positive integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")