#!/usr/bin/python3
for left in range(0, 10):
    for right in range(left+1, 10):
        if left == 8 and right == 9:
            print("{}{}".format(left, right), end="\n")
        elif left == right or right == left:
            continue
        else:
            print("{}{}".format(left, right), end=", ")
