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
    def size(self, value):
        """Checking the property size for errors"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Getting the area of the square"""
        return (self.__size * self.__size)
    def my_print(self):
        if (self.__size == 0):
            print ("")
        else:
            for row in range(self.__size):
                print("#" * self.__size)
