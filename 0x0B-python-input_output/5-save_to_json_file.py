#!/usr/bin/python3
""" module: working with JSON """


import json


def save_to_json_file(my_obj, filename):
    """
    serializes object to json string and writes it to a file.
    Both the file and obj are passed to the function as arguments
    """

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
