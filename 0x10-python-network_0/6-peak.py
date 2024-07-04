#!/usr/bin/python3
# finds the peak in a list of unsorted intergers


def find_peak(list_of_integers):
    """
    takes a list of integers as an argument
    finds the peak; largest number in the list
    """
    if len(list_of_integers) == 0:
        return None

    peak = 0
    for i in list_of_integers:
        if (i > peak):
            peak = i

    return (peak)
