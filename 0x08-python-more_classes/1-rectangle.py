#!/usr/bin/python3
""" a class that defines a rectangle """


class Rectangle:
    """
    creates a rectangle

    Args:
        width (int) : defines the width of the rectangle
        height (int) : defines the height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """
        initializes instance attributes for width and height
        """

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def width(self):
        """
        getter used to retrieve the dimensions of width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        sets the value for width

        Args:
        value (int) : holds value to be set for width
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        getter used to retrieve the dimensions of height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        sets the value for height

        Args:
        value (int) : holds value to be set for height
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
