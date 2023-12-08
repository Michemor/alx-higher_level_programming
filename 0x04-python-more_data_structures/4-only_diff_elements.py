#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    returns a set containing elements present in either set_1
    or set_2 but not both
    Input: set_1, set_2
    Output: set_3 contains unique elements
    """
    set_3 = set_1 ^ set_2
    return set_3
