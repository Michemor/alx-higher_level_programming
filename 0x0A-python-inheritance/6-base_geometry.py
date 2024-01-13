#!/usr/bin/python3
""" module: inheritance in python creating base class """


class BaseGeometry:
    """
    class containing attributes and methods assosiated to geometry
    """

    def area(self):
        """
        calculates area for geometric shape
        """
        raise Exception("area() is not implemented")
