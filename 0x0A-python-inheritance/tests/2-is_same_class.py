#!/usr/bin/python3
""" module: inheritance in python """


def is_same_class(obj, a_class):
    """
    checks whether an object is an instance of a class
    """
    if type(obj) is a_class:
        return True
    else:
        return False
