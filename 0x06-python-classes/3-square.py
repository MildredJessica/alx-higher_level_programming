#!/usr/bin/python3
class Square():
    """Creates a square"""
    __size = None
    
    def __init__(self, size=0):
        """Initialization of private instance attribute
            Args:
                size (int): The size of the square
        """
        if not isinstance(size, int):
                raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        """Calculates the area of a square
        
            Return: The current square area
        """
        return self.__size * self.__size
