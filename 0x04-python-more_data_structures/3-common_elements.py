#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    returns a set containing common elemets in set1 and set2
    Input: set1 and set2
    Output: set containing unique elements
    """
    set3 = set_1 & set_2
    return set3
