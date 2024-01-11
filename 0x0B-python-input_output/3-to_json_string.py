#!/usr/bin/python3
""" module: working with json (JavaScript Object Notation) """

import json


def to_json_string(my_obj):
    """ 
    converts an object to a json string. The object is passed
    as an argument to the string
    """
    return json.dumps(my_obj)
