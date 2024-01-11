#!/usr/bin/python3
""" module: working with JSON """

import json


def from_json_string(my_str):
    """ converts from json string back to python object, the string is
    passed as a argument to this function
    """
    return json.loads(my_str)
