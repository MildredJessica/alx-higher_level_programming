#!/usr/bin/python3
for num in range(10):
    for s in range(10):
        if s == 9 and num == 9:
            print("{}{}".format(num, s))
        else:
            print("{}{}".format(num, s), end=', ')
