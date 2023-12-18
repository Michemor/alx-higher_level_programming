#!/usr/bin/python3
def safe_print_division(a, b):
    """
    prints division of two numbers and checks for any
    exceptions
    """
    result = None
    try:
        result = a / b
        return (result)
    except Exception:
        return (None)
    finally:
        print("Inside result {}".format(result))
