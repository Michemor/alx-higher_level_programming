#!/usr/bin/python3
def islower(c):
    """
    function is lower checks if parsed character is lowercase
    Input: c a lower character
    Output: returns true of lower and false if otherwise
    """
    unicode_val = ord(c)
    for i in range(97, 123):
        if unicode_val == i:
            return True
    else:
        return False
