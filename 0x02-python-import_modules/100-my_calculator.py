#!/usr/bin/python3

if __name__ == "__main__":
    """Imports all functions from the file
    calculator_1.py and handles basic operations"""
    from calculator_1 import add, sub, div, mul
    import sys

    count = len(sys.argv) - 1
    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    op = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] in list(op.keys()):
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        print("{} {} {} = {}".format(a, sys.argv[2], b, op[sys.argv[2]](a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
