#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    sorts list in ascending order and then checks for unique elements
    then adds the unique elements
    Input: my_list
    Output: sum of unique list
    """
    unique_set = set(my_list)
    new_list = list(unique_set)

    return sum(i for i in new_list)
