#!/usr/bin/python3

def magic_calculation(a, b, c):
    """Does exactly the same as the following Python bytecode"""
    if a < b:
        return c
    elif c > b:
        return (a + b)
    return (a * b - c)
