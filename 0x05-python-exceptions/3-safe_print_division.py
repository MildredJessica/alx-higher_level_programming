#!/usr/bin/python3
def safe_print_division(a, b):
    """Divides 2 integers and prints the result"""
    div = None
    try:
        div = a / b
        return div
    except ZeroDivisionError:
        return div
    finally:
        print("Inside result: {}".format(div))
