#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matri"""
    return ([list(map(lambda a: a*a, row)) for row in matrix])
