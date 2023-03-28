#!/usr/bin/python3

from sys import stderr

import sys

def safe_print_integer_err(value):
    """A function that prints an integer."""
    try:
        print("{:d}".format(value))
        return True
    except Exception as ex:
        sys.stderr.write("Exception:" + str(ex) + "\n")
    return False
