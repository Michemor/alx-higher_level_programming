#!/usr/bin/python3
import sys
if __name__ = "__main__":
    ac = (len(sys.argv) - 1)
    argv = sys.argv
    if ac == 0:
        print("{} arguments.".format(ac), end="\n")
    elif ac == 1:
        print("{} argument".format(ac), end="\n")
        print("{}: {}".format(ac, argv[1]), end="\n")
    elif ac > 1:
        print("{} arguments:".format(ac), end="\n")
        for i in range(1, (ac + 1)):
            print("{}: {}".format(i, argv[i]), end="\n")

