#!/usr/bin/python3
"""Creating of a Class Rectangle"""


class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__height = value
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("width must be an integer")
        else:
            self.__width = value
