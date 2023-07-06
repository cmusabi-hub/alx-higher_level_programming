#!/usr/bin/python3
"""Definition of a class"""


class Square:
    """Creating class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialization of the variables"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get or sets the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Gets the position of coordinates"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets the position of the coordinates"""
        if (not isinstance(value, tuple)
                or len(value) != 2 or
                not all(isinstance(coord, int) for coord in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Gets the area of a square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square with # sign"""
        if (self.__size == 0):
            print()
        else:
            for point in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
