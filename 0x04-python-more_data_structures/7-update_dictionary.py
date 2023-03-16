#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """Replaces or adds a key, value to a dictionary"""
    if key not in a_dictionary.keys():
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
    return a_dictionary
