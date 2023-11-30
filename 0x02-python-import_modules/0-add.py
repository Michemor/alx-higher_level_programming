#!/usr/bin/python3
import add_0 as plus

if __name__ == "__main__":
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, plus.add(a, b)), end="\n")
