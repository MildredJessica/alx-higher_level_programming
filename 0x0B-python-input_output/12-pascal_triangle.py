#!/usr/bin/python3
"""Returns a list of lists of integers"""


def pascal_triangle(n):
    """Returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    li = []
    if n <= 0:
        return li
    for i in range(n):
        li.append([])
        li[i].append(1)
        for k in range(1, i):
            li[i].append(li[i - 1][k - 1] + li[i - 1][k])
        if i != 0:
            li[i].append(1)
    return li
