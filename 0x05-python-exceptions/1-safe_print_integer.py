#!/usr/bin/python3

def safe_print_integer(value):
    "Prints an integer with {:d}.format()"
    bol = False
    try:
        print("{:d}".format(value))
        bol = True
    except ValueError:
        bol = False
    return bol
