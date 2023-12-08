#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    updates value of key in dictionary if it exists, creates new key
    if it doesnt exist in dictionary
    Input: a_dictionary, key to be updates and its value
    Output: new a_dictionary
    """
    if key not in a_dictionary:
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
    return a_dictionary
