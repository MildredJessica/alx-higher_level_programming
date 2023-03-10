#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the results of all arguments of the command line"""
    import sys
    count = len(sys.argv) - 1
    sum = 0
    for i in range(count):
        sum += int(sys.argv[i + 1])
    print("{}".format(sum))
