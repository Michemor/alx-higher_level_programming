#!/usr/bin/python3
"""
module: working with inheritance in python
and other examples of concepts in python programming
"""


def is_same_class(obj, a_class):
    """
    checks whether an object is an instance of a class
    both object and the class are passed as arguments
    """
    if type(obj) is a_class:
        return True
    else:
        return False
