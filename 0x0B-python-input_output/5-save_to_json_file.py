#!/usr/bin/python3
""" module: working with JSON """


import json


def save_to_json_file(my_obj, filename):
    """
    serializes object to json string and writes it to a file.
    Both the file and obj are passed to the function as arguments
    """
    obj_to_str = json.dumps(my_obj)

    with open(filename, 'w') as f:
        f.write(obj_to_str)
