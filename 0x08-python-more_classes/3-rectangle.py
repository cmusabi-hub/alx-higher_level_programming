#!/usr/bin/python3
"""Creating a Class"""


class Rectangle:
    """"Class rectangle"""

    def __init__(self, width=0, height=0):
        """Initialization of variables"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property retriver"""
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Property retriver"""
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Area of the Rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Perimeter of the rectangle"""
        return ((self.__height + self.__width) * 2)

    def __str__(self):
        """Returns a string of created triangle using # sign"""
        return "\n".join(["#" * self.width for row in range(self.height)])
