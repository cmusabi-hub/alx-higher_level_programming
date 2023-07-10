#!/usr/bin/python3
"""Creation of a class"""


class Rectangle:
    """Definition of class"""

    def __init__(self, width=0, height=0):
        """Initialization of Variables"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property retriver"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter"""
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
        """Property Setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Gets area of rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Gets perimeter of rectangle"""
        if (self.__height == 0 or self.__width == 0):
            return 0
        return ((self.__height + self.__width) * 2)
