#!/usr/bin/python3
"""An Empty class"""


class BaseGeometry:
    """An empty BaseGeometry class"""
    
    def __init__(self):
        """Empty Instance"""
        pass

    def area(self):
        """Definces a public instance method"""
        raise Exception("area() is not implemented")
