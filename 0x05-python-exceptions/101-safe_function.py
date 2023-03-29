#!/usr/bin/python3

import sys
from unittest import result


def safe_function(fct, *args):
    """A function that executes a function safely"""
    result = None
    try:
        result = fct(*args)
    except Exception as ex:
        sys.stderr.write("Exception: " + str(ex) + "\n")
    return result
