#!/usr/bin/python3
class Square():
    """Creates a square
    """
    __size = None
    __position = None
    
    def __init__(self, size=0, position=(0, 0)):
        """Initialization of private instance attribute
            Args:
                size (int): The size of the square
                position (int, int): The positions of the square
        """
        self.__size = size
        self.__position = position
    
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
    
    @property
    def position(self):
        """Retrieves the position of the square
           Returns: The position of the square
        """
        return self.__position
    
    @position.setter
    def position(self, value):
        """ Changes the value of size
        Args:
            value (int): The new size of the square
        """
        if not isinstance(value, tuple):
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of a square
            Returns: The current square area
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints in stdout the square with the character #
        """
        if self.__size == 0:
            print("\n")
            return
        for row in range(self.__position[1]):
            print("")
            
        for column in range(self.size):
                print("{}{}".format(" " * self.__position[0], '#' * self.__size))
