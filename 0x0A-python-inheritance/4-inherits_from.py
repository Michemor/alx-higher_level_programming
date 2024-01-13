#!/usr/bin/python3
""" module: inheritance in python, checks whether the class
has been inherited from another class
"""


def inherits_from(obj, a_class):
    """
    checks whether a class is inherited from another class
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
