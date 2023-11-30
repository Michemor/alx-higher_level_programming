#!/usr/bin/python3
def uppercase(str):
    """
    function converts string to uppercase
    Input: str
    Output: prints string
    """
    for n in str:
        if ord(n) >= 97 and ord(n) <= 122:
            temp = chr(ord(n) - 32)
        else:
            temp = n
        print("{}".format(temp), end="")
    print("\n".format(), end="")
