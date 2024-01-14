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

    def area(self):
        """
        calculates area of a rectangle
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        prints information about a rectangle passed
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
