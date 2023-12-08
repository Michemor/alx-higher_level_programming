#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    searches for an element (search) in a list and replaces it (replace)
    Input: my_list
    Output: new replaces list
    """
    new_list = []
    for i in my_list:
        if i == search:
            i = replace
        new_list.append(i)
    return new_list
