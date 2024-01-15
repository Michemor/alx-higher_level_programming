#!/usr/bin/python3
""" module : base class to be used to instatiate other objects """


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
