#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers"""
    if len(matrix) <= 0:
        print("$")
    else:
        for i in matrix:
            for s in i:
                print("{:d}".format(s), end=" " if s != i[-1] else "")
            print()
