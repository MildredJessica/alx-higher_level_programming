#!/usr/bin/python3
"""Method to read a text file"""


def read_file(filename=""):
    """Reads from a text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
