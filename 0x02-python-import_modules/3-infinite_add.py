#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ac = len(argv)
    add = 0
    for i in range(1, ac):
        if (isinstance(int(argv[i]), (int))):
            add += int(argv[i])
    print("{}".format(add), end="\n")
