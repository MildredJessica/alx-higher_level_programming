#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the number of and the list of its arguments."""
    import sys
    count = len(sys.argv)
    num = 1
    if count == 0:
        print("{} arguments.".format(count - 1))
    elif count == 1:
        print("{} argument:".format(count - 1))
        print("{}: {}".format(num, sys.argv[1]))
    else:
        print("{} arguments:".format(count - 1))
        while num != count:
            print("{}: {}".format(num, sys.argv[num]))
            num += 1
