#!/usr/bin/python3
"""Function definition"""


def print_square(size):
    """Prints square with #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    new_square = (("#" * size) for row in range(size))

    for row in new_square:
        print(row)
