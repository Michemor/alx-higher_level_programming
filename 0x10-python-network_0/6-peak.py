#!/usr/bin/python3
# finds the peak in a list of unsorted intergers


def find_peak(list_of_integers):
    """
    takes a list of integers as an argument
    finds the peak; largest number in the list
    """
    list_len = len(list_of_integers)
    if list_len <= 0:
        return None

    for i in range(list_len):
        sorted = True
        for j in range(list_len - i - 1):
            if (list_of_integers[j] > list_of_integers[j + 1]):
                temp = list_of_integers[j]
                list_of_integers[j] = list_of_integers[j + 1]
                list_of_integers[j + 1] = temp
                sorted = False
        if sorted:
            break

    return (list_of_integers[list_len - 1])
