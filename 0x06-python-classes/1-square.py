#!/usr/bin/python3
class Square():
    """Creates a square"""
    __size = None
    
    def __init__(self, size):
        """Initialization of private instance attribute
            Args:
                size (int): The size of the square
        """
        self.__size = size
