#!/usr/bin/python3
"""Inherits from the base geometry class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """Instantiates the width and height of the rectangle
        Args:
        width (int): The width of the rectangle
        height (int): The height of the rectangle
        """
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height

    def area(self):
        """Calculates the area""" 
        return self.__width * self.__height    

    def __str__(self):
        """Prints the rectangle description"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)