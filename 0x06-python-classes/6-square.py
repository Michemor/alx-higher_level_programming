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
    def __init__(self, size=0, position=(0, 0)):
        """
        initializes the dimensions of a square
        as contained in size

        Args:
             size (int): width of square
             position (tuple): 2 integers indicating where
                               spaces will be filled
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if (not isinstance(position, tuple) or
                len(position) != 2 or
            not all(isinstance(n, int) for n in position) or
            not all(n >= 0 for n in position)):
            raise TypeError(
                    "position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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
                [print(" ", end="")for j in range(self.__position[0])]
                [print("#", end="")for j in range(self.__size)]
                print("", end="\n")

    @property
    def position(self):
        """
        retrieves the value of position attribute
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        setter method: position
        sets the value of position

        Return:
        returns the value of position
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
            not all(isinstance(n, int) for n in value) or
            not all(n >= 0 for n in value)):
            raise TypeError(
                    "position must be a tuple of two positive integers")
