#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element in a list based on a certain position"""
    if idx < 0 or idx > len(my_list) - 1:
        return None
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
