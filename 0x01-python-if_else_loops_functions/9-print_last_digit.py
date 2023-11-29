#!/usr/bin/bash
def print_last_digit(number):
    """
    function prints the last digit of given number
    Input: number
    Output: prints the digit
    """
    if number <= 9 and number >= 0:
        print("{}".format(number), end="")
    else:
        store_mod = abs(number) % 10
        print("{}".format(store_mod), end="")
    
