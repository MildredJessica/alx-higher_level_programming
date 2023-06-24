#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """An empty class that represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialises a new Rectangle.
        Args:
        width (int): The width of the rectangle
        height (int): THe height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Changes the width of the rectangle
        Args:
        value (int): The size of the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Changes the height of the rectangle
        Args:
        value (int): The size of the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of a rectangle"""
        peri = 0
        if self.__width == 0 or self.__height == 0:
            peri = 0
        else:
            peri = 2 * (self.__width + self.__height)
        return peri
