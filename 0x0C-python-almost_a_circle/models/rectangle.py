#!/usr/bin/python3
"""
This module defines the Rectangle class, which is a subclass of the Base class.
It provides attributes to represent a rectangle's dimensions and position,
as well as methods to calculate its area, display a visual representation,
and update its attributes dynamically. The Rectangle class ensures proper
data validation to handle errors in input values and prevent invalid configurations.

Classes:
    Rectangle - Represents a rectangle, including dimensions and position.
"""

from base import Base


class Rectangle(Base):
    """
    The Rectangle class represents a geometric rectangle shape.
    It inherits from the Base class, allowing it to have a unique ID.

    Attributes:
        width (int): The width of the rectangle, must be a positive integer.
        height (int): The height of the rectangle, must be a positive integer.
        x (int): The x-coordinate of the rectangle, must be a non-negative integer.
        y (int): The y-coordinate of the rectangle, must be a non-negative integer.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle, must be > 0.
            height (int): The height of the rectangle, must be > 0.
            x (int): The x-coordinate for rectangle position, must be >= 0.
            y (int): The y-coordinate for rectangle position, must be >= 0.
            id (int, optional): The unique identifier for the rectangle.

        Raises:
            TypeError: If any attribute is not an integer.
            ValueError: If width/height <= 0 or x/y < 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle, ensuring it's a positive integer."""
        self.validator('width', value)
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle, ensuring it's a positive integer."""
        self.validator('height', value)
        self.__height = value

    @property
    def x(self):
        """Gets the x-coordinate of the rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x-coordinate, ensuring it's a non-negative integer."""
        self.validator('x', value)
        self.__x = value

    @property
    def y(self):
        """Gets the y-coordinate of the rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y-coordinate, ensuring it's a non-negative integer."""
        self.validator('y', value)
        self.__y = value

    @staticmethod
    def validator(name, value):
        """
        Validates input for the attributes to ensure they are within required constraints.

        Args:
            name (str): The name of the attribute (width, height, x, y).
            value (int): The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If width or height is <= 0, or if x or y is < 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if (name == 'width' or name == 'height') and value <= 0:
            raise ValueError(f"{name} must be > 0")
        if (name == 'x' or name == 'y') and value < 0:
            raise ValueError(f"{name} must be >= 0")

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Prints a visual representation of the rectangle using the '#' character,
        taking into account the x and y positions for alignment.
        """
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Provides a string representation of the Rectangle instance.

        Returns:
            str: A formatted string representation.
        """
        return f"[{type(self).__name__}] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args):
        """
        Updates the attributes of the rectangle using positional arguments.

        Args:
            *args (int): A variable number of arguments that match the attributes in order:
                         id, width, height, x, y.
        """
        attrs = ['id', 'width', 'height', 'x', 'y']
        for i, value in enumerate(args):
            setattr(self, attrs[i], value)
