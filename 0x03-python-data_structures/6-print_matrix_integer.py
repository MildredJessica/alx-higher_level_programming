#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers"""
    if len(matrix) <= 0:
        print("$")
    else:
        for i in range(len(matrix)):
            for s in range(len(matrix[i])):
                if s == len(matrix) - 1:
                    print(matrix[i][s], end="$")
                else:
                    print(matrix[i][s], end=" ")
            print("")
