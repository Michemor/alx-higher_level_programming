#!/usr/bin/python3
""" Rectangle: inherits from base """
from .base import Base


class Rectangle(Base):
    """
    Rectangle: inherits methods and attributes from base
    Also defines its own unique attributes
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initializes a Rectangle object

        Args:
            width: width of rectangle
            height: height of the rectangle
            x:
            y:
            id: identifier of a rectangle
        """
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def __str__(self):
        """
        overrides the original str() method and prints
        dev defined string
        """
        return (
                "[Rectangle] ({}) {}/{} - {}/{}".format(
                    self.id, self.__x, self.__y, self.__width, self.__height
                )
            )

    @property
    def width(self):
        """
        retrieves the value of width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        sets the dimensions of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        retrieves the dimensions of height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        sets the value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        retrieves the value of x
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        sets the value of x passed as an argument
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        retrieves the value of y
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        sets the value of y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        calculates the area of a rectangle

        Return:
            the area of the rectangle
        """
        return (self.__width * self.__height)

    def display(self):
        """
        prints to stdout the Rectangle instance with the character #
        """
        for s in range(self.__y):
            print()
        for c in range(self.__height):
            print(" " * self.__x, end="")
            for r in range(self.__width):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        """
        updates the value of rectangle attributes
        using arbitrary arguments
        """
        if args:
            self.id = args[0] if len(args) > 0 else self.id
            self.width(args[1]) if len(args) > 1 else self.width
            self.height(args[2]) if len(args) > 2 else self.height
            self.x(args[3]) if len(args) > 3 else self.x
            self.y(args[4]) if len(args) > 4 else self.y
        if kwargs:
            self.id = kwargs.get("id", self.id)
            self.width = kwargs.get("width", self.width) 
            self.height = kwargs.get("height", self.height) 
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)
