#!/usr/bin/python3
""" this class defines a class that sorts contents of a list """


class MyList(list):

    def __init__(self):
        """
        initializes the class when created
        """
        super().__init__()

    def print_sorted(self):
        """
        print_sorted - prints a list containing ints sorted
        in ascending order
        """
        print(sorted(self))
