#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """check whether contents of a list are divisible by 2 or not"""
    new_list = my_list.copy()

    for i in range(len(new_list)):
        if (new_list[i] % 2) == 0:
            new_list[i] = True
        else:
            new_list[i] = False
    return (new_list)
