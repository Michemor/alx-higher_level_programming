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
    def __init__(self, size):
        """
        initializes the dimensions of a square
        as contained in size

        Args:
             size (int): width of square
        """
        self.__size = size
