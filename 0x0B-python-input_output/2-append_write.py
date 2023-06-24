#!/usr/bin/python3
"""Appends to a text file"""


def append_write(filename="", text=""):
    """Appends a string to a file"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
