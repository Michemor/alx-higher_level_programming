#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    print_list_integer: prints integers line by line
    Input: my_list, list containing integers
    Output: integers printed line by line
    """
    for i in range(len(my_list)):
        print("{}".format(my_list[i]), end='\n')
