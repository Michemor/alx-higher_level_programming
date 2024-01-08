#!/usr/bin/python3
""" Defines a function that lists the attributes and methods of an object """

def lookup(obj):
    """
    lists the available attributes and methods of an object

    Returns: list
    """
    return (dir(obj))
