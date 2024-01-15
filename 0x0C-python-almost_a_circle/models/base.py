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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        - list_objs is a list of instances who inherits of Base
        - example: list of Rectangle or list of Square instances
        - If list_objs is None, save an empty list
        - The filename must be: <Class name>.json - example: Rectangle.json
        - You must use the static method to_json_string (created before)
        - You must overwrite the file if it already exists
        """

        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                dicts = [objs.to_dictionary() for objs in list_objs]
                file.write(Base.to_json_string(dicts))
