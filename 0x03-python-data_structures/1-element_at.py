#!/usr/bin/python3
def element_at(my_list, idx):
    """
    element_at: prints element at idx
    Input: my_list, contains list of integers
           idx, position of index to be retrieved
    Output: index at idx
    """
    if idx < 0:
        return (None)
    elif idx >= len(my_list):
        return (None)
    for i in range(len(my_list)):
        if idx == i:
            return (my_list[i])
