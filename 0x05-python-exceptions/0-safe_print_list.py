#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list"""
    count = 0
    try:
        while (count != x):
            print("{:d}".format(my_list[count]), end="")
            count += 1
    except IndexError:
        pass
    print()
    return count
