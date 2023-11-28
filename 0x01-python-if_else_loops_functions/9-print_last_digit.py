#!/usr/bin/bash
def print_last_digit(number):
    """
    function prints the last digit of given number
    Input: number
    Output: prints the digit
    """
    store_mod = number - (number // 10) * 10
    print("{}".format(store_mod), end="")
