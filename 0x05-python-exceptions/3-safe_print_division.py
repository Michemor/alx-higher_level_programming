#!/usr/bin/python3
def safe_print_division(a, b):
    """
    prints division of two numbers and checks for any
    exceptions
    """
    try:
        result = a / b
    except (ValueError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
