#!/usr/bin/python3
"""Definition of a Class"""


class Square:
    """Creating square class"""
    def __init__(self, size=0):
        """Initialization of variables size of the new square"""
        self.size = size

    @property
    def size(self):
    """Defining the property size"""
        return self.__size
    @size.setter

    def size(self, size):
    """Checking the property size for errors"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
    """Getting the area of the square"""
        return (self.size * self.size)
