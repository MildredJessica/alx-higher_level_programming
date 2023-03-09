#!/usr/bin/python3
import sys

count = len(sys.argv)
num = 1
if count == 1:
    print("{} arguments.".format(count - 1))
elif len(sys.argv) == 2:
    print("{} argument:".format(count - 1))
    print("{}: {}".format(num, sys.argv[1]))
else:
    print("{} arguments:".format(count - 1))
    while num != count:
        print("{}: {}".format(num, sys.argv[num]))
        num += 1
