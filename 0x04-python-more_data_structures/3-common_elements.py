#!/usr/bin/python3

def common_elements(set_1, set_2):
    """Returns a set of common elements in two sets"""
    set_list = []
    for i in set_1:
        if i in set_2:
            set_list.append(i)
    return (set_list)
