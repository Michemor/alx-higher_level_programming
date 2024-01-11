#!/usr/bin/python3
""" module: working with json """
import json


def load_from_json_file(filename):
    """
    creates an object from a json file passed to it as an argument
    """
    with open(filename, 'r') as f:
        return json.load(f)
