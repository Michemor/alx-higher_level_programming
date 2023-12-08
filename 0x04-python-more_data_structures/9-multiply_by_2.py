#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    multiplies the values of each by key by 2
    """
    mult_dict = {}
    for k, v in a_dictionary.items():
        v *= 2
        mult_dict[k] = v
    return mult_dict
