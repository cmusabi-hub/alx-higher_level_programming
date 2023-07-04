#!/usr/bin/python3
""" Definition of a class Square"""


class Square:
    """ Initialization of variables"""
    def __init__(self, size=0):
        """ Initialization of variable size
        the size should be integer type.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
