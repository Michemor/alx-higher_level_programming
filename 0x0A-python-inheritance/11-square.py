#!/usr/bin/python3
""" module: inheritance from Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    inherits from rectangle and implements its methods
    and getters
    """

    def __init__(self, size):
        """
        instantiates square method its dimensions

        Args:
            size(int) : defines dimensions of a square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        defines calculation for area method
        """
        return (self.__size * self.__size)

    def __str__(self):
        """
        prints info about square
        """
        return ("[Recangle] {}/{}".format(self.__size, self.__size))
