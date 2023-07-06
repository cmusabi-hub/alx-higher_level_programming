#!/usr/bin/python3
"""Creating of a class"""


class Square:
    """Defining class Square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif(value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size == value
    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or not len(value) != 2 or not all(isinstance(coord, int) for coord in value) or not all(coord >= 0 for coord in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        else:
            self.__position = value
    def area(self):
        return (self.__size * self.__size)
    def my_print(self):
        if (self.__size == 0):
            print()
        else:
            for point in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
