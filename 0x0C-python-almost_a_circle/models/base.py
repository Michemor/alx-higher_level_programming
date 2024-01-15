#!/usr/bin/python3
""" module : base class to be used to instatiate other objects """
import json


class Base:
    """
    Base class
    Contains attributes and methods to be inherited
    by all other objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialize an object with value id

        Args:
            id (int) : identifier of the object
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base. __nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        this is a static method
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return (json.dumps(list_dictionaries))
