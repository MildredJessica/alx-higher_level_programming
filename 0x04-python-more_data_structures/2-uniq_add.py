#!/usr/bin/python3
from functools import reduce
def uniq_add(my_list=[]):
    """Adds all unique integers in a list """
    sum = 0
    sum = reduce(lambda n,y: y + n, list(set(my_list)))
    return sum