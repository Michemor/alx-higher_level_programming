#!/usr/bin/python3
"""
A simple square

Attributes:
    size: defines the dimensions of a square
"""


class Square:
    """
    A simple square

    """
    def __init__(self, size=0):
        """
        initializes the dimensions of a square
        as contained in size

        Args:
             size (int): width of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        area : computes the area of a square based on
        dimensions given by __init__

        Return:
        The area of the square
        """
        return (self.__size * self.__size)
