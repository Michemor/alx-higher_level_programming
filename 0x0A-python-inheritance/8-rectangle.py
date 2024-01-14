#!/usr/bin/python3
""" module: inheritance of Rectangle from BaseClass geometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class inherits from base geometry
    BaseGeometry is the parent class
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle class with dimensions
        width: size of the width
        height: size of the height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
