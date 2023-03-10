#!/usr/bin/python3
"""Prints the ASCII alphabet, in reverse order, alternating lowercase
and uppercase (z in lowercase and Y in uppercase) , not
followed by a new line."""
ch = 0
for i in range(122, 96, -1):
    if i % 2 == 1:
        ch = 32
    else:
        ch = 0
    print("{}".format(chr(i - ch)), end="")
