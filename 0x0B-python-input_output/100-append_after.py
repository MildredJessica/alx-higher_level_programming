#!/usr/bin/python3
"""Inserts a line of text to a file, after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file,
    after each line containing a specific string"""
    with open(filename, encoding='utf-8') as f:
        li = f.readlines()

    with open(filename, 'w', encoding='utf-8') as f:
        for st in li:
            if search_string in st:
                st += new_string
            f.write(st)
