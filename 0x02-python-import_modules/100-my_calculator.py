#!/usr/bin/python3

if __name__ == "__main__":
    """Imports all functions from the file
    calculator_1.py and handles basic operations"""
    from calculator_1 import add, sub, div, mul
    import sys

    count = len(sys.argv)
    for i in range(count):
        print("{} {}". format(i, sys.argv[i]))
    op = {"+": add, "-": sub, "s*": mul, "/": div}
    if sys.argv[2] not in list(op.keys()):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, op[sys.argv[2]](a, b)))
