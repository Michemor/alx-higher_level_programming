#!/usr/bin/python3
def safe_print_integer(value):
    """
    prints an integer: checks whether the passed value
    is an integer and prints it
    """
    try:
        print("{:d}".format(value), end="\n")
        return (True)
    except Exception:
        return (False)
