#!/usr/bin/python3
class Square():
    """Creates a square"""
    __size = None
    
    def __init__(self, size=0):
        """Initialization of private instance attribute
            Args:
                size (int): The size of the square
        """
        self.__size = size
    
    @property
    def size(self):
        """Retrieves the size of the square
           Returns: The size of the square
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """ Changes the value of size
        Args:
            value (int): The new size of the square
        """
        if not isinstance(value, int):
                raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of a square
            Returns: The current square area
        """
        return self.__size * self.__size
