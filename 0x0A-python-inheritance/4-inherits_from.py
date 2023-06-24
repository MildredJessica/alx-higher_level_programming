#!/usr/bin/python3
"""Checks if the object is an instance of a class that
inherited (directly or indirectly) from the specified class """


def inherits_from(obj, a_class):
    """Returns True of false if an object is an
    instance of class (directly or indirectly)
    Args
        obj: object
        a_class: class
    """
    return issubclass(type(obj), a_class) and (type(obj) != a_class)
