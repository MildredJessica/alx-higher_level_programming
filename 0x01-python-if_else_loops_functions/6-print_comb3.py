#!/usr/bin/python3
for num in range(0, 10):
    for s in range(num + 1, 10):
        if s == 9 and num == 8:
            print("{}{}".format(num, s))
        else:
            print("{}{}".format(num, s), end=', ')
