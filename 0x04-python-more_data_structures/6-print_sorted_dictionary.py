#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys"""
    for i, y in sorted(a_dictionary.items()):
        print("{}: {}". format(i, y))
