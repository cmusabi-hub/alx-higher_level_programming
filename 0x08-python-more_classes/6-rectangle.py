#!/usr/bin/python3
"""Creating of a class"""


class Rectangle:
    """Creating class REctangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialization of variables"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            raise ValueError("height must be >= 0")
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
        """Gets area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Gets Perimeter of the rectangle"""
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """Prints the rectangle"""
        return ("\n".join(["#" * self.__width
                           for row in range(self.__height)]))

    def __repr__(self):
        """Returns a string representation of the rectangle
        to be able to recreatea new instance by using eval()"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Cleans up memory"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
