#!/usr/bin/python3
def print_last_digit(number):
    """
    function prints the last digit of given number
    Input: number
    Output: prints the digit
    """
    if number >= 0:
        last_dig = number % 10
    elif number < 0:
        last_dig = (number * -1) % 10

    print("{}".format(last_dig), end="")
    return last_dig
