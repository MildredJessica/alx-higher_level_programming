#!/usr/bin/python3
"""Rectangle Class"""

from models.base import Base


class Rectangle(Base):
    """The Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialises a new Rectangle
        Args:
        width (int): the width of the rectangle
        height (int): Height of the rectangle
        x (int): The x cordinate of the rectangle
        y (int): THe y cordinate of the rectangle
        id (int): The id of the rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
