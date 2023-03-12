#!/usr/bin/python3

def no_c(my_string):
    """Removes character c and C from my_string"""
    return ("".join(x for x in my_string if x != 'c' and x != 'C'))
