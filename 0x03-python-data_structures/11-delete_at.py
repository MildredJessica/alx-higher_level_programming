#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific position in a list"""
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    new_list = my_list.copy()
    new_list.remove(new_list[idx])
    return new_list
