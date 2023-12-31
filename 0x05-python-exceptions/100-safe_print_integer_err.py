#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """
    prints integers: in case value is not integer
    error is printed on stderr
    """
    try:
        print("{:d}".format(value))
        return (True)
    except TypeError as e:
        print("Exception: {}".format(e), file=sys.stderr, end="\n")
        return (False)
    except ValueError as e:
        print("Exception: {}".format(e), file=sys.stderr, end="\n")
        return (False)
