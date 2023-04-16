#!/usr/bin/python3
"""Returns a dictionary description"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    Args
    obj (object)
    """
    return obj.__dict__