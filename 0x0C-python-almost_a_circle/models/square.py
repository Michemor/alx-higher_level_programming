#!/usr/bin/python3
""" square: inherits from python """
from .base import Base
from .rectangle import Rectangle


class Square(Rectangle):
    """
    square: defines a square that inherits some properties
    from a rectangle while also adds its own unique attributes
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        initializes an object with values of size, x, y and
        id attributes
        """
        super().__init__(size, size, x, y, id)
        self.width = size

    @property
    def size(self):
        """
        getter method: returns the value of size
        """
        return (self.width)

    @size.setter
    def size(self, value):
        """
        sets the value of the width which equates
        to the value of the square
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        prints info about square. Overrides the str() method
        and prints dev defined info
        """
        return (
                "[Square] ({}) {}/{} - {}".format(
                    self.id, self.x, self.y, self.size
                    )
                )

        def update(self, *args, **kwargs):
            """
            updates dimensions of square based on args and kwargs
            These are arbitrary arguments that allow us to pass
            a random number of arguments to a function
            """
            if args:
                self.id = args[0] if len(args) > 0 else self.id
                self.size = args[1] if len(args) > 1 else self.size
                self.x = args[2] if len(args) > 2 else self.x
                self.y = args[3] if len(args) > 3 else self.y
            if kwargs:
                self.id = kwargs.get("id", self.id)
                self.size = kwargs.get("size", self.size)
                self.x = kwargs.get("x", self.x)
                self.y = kwargs.get("y", self.y)

        def to_dictionary(self):
            """
            defines a dictionary representation of a square
            """
            square_dict = {}

            square_dict['id'] = self.id
            square_dict['size'] = self.size
            square_dict['x'] = self.x
            square_dict['y'] = self.y

            return (square_dict)
