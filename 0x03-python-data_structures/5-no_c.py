#!/usr/bin/python3
import re


def no_c(my_string):
    return ("".join(x for x in my_string if x != 'c' and x != 'C'))
