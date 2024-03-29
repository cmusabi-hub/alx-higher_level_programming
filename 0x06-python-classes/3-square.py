#!/usr/bin/python3
"""Definition of a class Square"""


class Square:
    """Class Square"""

    def __init__(self, size=0):
        """Initialization of variable size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Instace gets area of the square"""
        return (self.__size * self.__size)
