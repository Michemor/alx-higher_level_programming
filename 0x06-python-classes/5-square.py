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

    @property
    def size(self):
        """
        returns the attribute size
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        sets the size variable according to passed parameter

        Args:
            size: dimension of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def my_print(self):
        """
        prints the square using the # character
        """
        if self.__size <= 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("", end="\n")
