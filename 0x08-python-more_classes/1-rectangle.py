#!/usr/bin/python3
"""Creating of a Class Rectangle"""


class Rectangle:

    """Defining class rectangle"""
    def __init__(self, width=0, height=0):
        """Initialization of variables"""
        self.width = width
        self.height = height

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
