#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """Returns a set of all elements present in only one set."""
    set_list = []
    for i in set_1:
        set_list.append(i)
    for i in set_2:
        if i not in set_list:
            set_list.append(i)
    return (set_list)
