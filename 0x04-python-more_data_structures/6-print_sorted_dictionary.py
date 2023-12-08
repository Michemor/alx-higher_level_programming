#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    sorts a dictionary
    Input: a_dictionary
    Output: sorted dictionary
    """
    for k, v in sorted(a_dictionary.items()):
        print("{}: {}".format(k, v))
