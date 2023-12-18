#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    prints some x elements from my_list
    and checks for exceptions caused using try/except block
    """
    num = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            num += 1
        except IndexError:
            break
    print()
    return (num)
