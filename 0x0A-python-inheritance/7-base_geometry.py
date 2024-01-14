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

    def integer_validator(self, name, value):
        """
        validates value and raises an exception when value is not
        an integer, or when value is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
