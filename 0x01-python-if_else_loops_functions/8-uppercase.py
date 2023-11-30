#!/usr/bin/python3
def uppercase(str):
    for n in str:
        if ord(n) >= 97 and ord(n) <= 122:
            temp = chr(ord(n) -32)
        else:
            temp = n

        print("{0}".format(temp), end="")
