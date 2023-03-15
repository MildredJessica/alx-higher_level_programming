#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another in a new list"""
    return ([list(map(lambda t: replace if t == search else t, my_list))])
