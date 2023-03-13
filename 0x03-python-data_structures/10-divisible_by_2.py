#!/usr/bin/python3
import re


def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list"""
    new_list = []
    if len(my_list) == 0:
        return my_list
    for n in range(len(my_list)):
        if (my_list[n] % 2) == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
