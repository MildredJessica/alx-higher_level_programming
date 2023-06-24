#!/usr/bin/python3
"""Inherits from list"""


class MyList(list):
    """Inherits form list and appends"""

    def __init__(self):
        """Initialises a new List
        """
        pass
    
    def print_sorted(self):
        """Sorts the list out"""
        new_list = list.copy(self)
        new_list .sort()
        print(new_list)
