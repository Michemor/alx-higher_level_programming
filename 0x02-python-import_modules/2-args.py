#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    ac = len(argv) - 1
    
    if ac == 0:
        print("{} arguments.".format(ac), end="\n")
    elif ac == 1:
        print("1 argument".format(), end="\n")
        print("1: {}".format(argv[1]), end="\n")
    elif ac > 1:
        print("{} arguments:".format(ac), end="\n")
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]), end="\n")
