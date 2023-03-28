#!/usr/bin/python3

from curses.ascii import isdigit


def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list and only integers"""
    count = 0
    for num in range(x):
        try:
            print("{:d}".format(my_list[num]), end = "")
        except (ValueError, IndexError, TypeError):
            pass
        else:
            count += 1
    print()
    return count
