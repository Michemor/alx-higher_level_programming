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

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        - json_string is a string representing a list of dictionaries
        - If json_string is None or empty, return an empty list
        - Otherwise, return the list represented by json_string
        """
        if json_string is None or json_string == "[]":
            return ([])
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        - **dictionary can be thought of as a double pointer to a dictionary
        - To use the update method to assign all attributes
        you must create a “dummy” instance before:
        - Create a Rectangle or Square instance with “dummy” 
        mandatory attributes (width, height, size, etc.)
        - Call update instance method to this “dummy” 
        instance to apply your real values
        - You must use the method def update(self, *args, **kwargs)
        **dictionary must be used as **kwargs of the method update
        - You are not allowed to use eval
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(2, 4)
            else:
                dummy = cls(1)

            dummy.update(**dictionary)

        return (dummy)
