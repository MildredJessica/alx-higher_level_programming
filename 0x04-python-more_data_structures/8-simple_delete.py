#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary"""
    if key in a_dictionary.keys():
        del a_dictionary[key]
    return a_dictionary
