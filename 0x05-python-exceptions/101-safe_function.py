#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    prints execution of function safely i.e

    1.unpacks the variables contained in *args
    2. checks whether the error that result is
       -ValueError
       -TypeError
       -ZeroDivisionError

    Return:
    on successful execution it returns the result of division
    on failure it returns None
    """
    try:
        x, y = args
        return (fct(x, y))
    except TypeError as e:
        print("Exception: {}".format(e), file=sys.stderr, end="\n")
        return (None)
    except ZeroDivisionError as e:
        print("Exception: {}".format(e), file=sys.stderr, end="\n")
        return (None)
    except IndexError as e:
        print("Exception: {}".format(e), file=sys.stderr, end="\n")
        return (None)
