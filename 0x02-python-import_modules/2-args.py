#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the number of and the list of its arguments."""
    import sys
    count = len(sys.argv) - 1
    if count == 0:
        print("{} arguments.".format(count))
    elif count == 1:
        print("1 argument:")
        print("{}: {}".format(count, sys.argv[1]))
    else:
        print("{} arguments:".format(count))
        for num in range(count):
            print("{}: {}".format(num + 1, sys.argv[num + 1]))
