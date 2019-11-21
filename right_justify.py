#!/usr/bin/env python3


def right_justify(s):
    size = 70 - len(s)
    justified = " " * size + s

    for i in range(1, 71):
        if(i % 10 == 0):
            print(int(i / 10), end='')
        else:
            print('-', end='')

    print("")
    print("Original Var:\n{0}\nNew Var:\n{1}".format(s, justified))
