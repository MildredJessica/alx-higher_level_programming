#!/usr/bin/python3
"""An Empty class"""


class BaseGeometry:
    """An empty BaseGeometry class"""
    def __init__(self):
        """Empty Instance"""
        pass

    def area(self):
        """Defines a public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates Value"""
        if type(value) != int:
            raise TypeError(name, "must be an integer")
        if value <= 0:
            raise ValueError(name, "must be greater than 0")
