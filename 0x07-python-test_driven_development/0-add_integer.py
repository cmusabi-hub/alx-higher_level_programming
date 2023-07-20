#!/usr/bin/python3
"""Defines integer addition"""


def add_integer(a, b=98):
    """Return the integer addition of parameters and b.
    Float arguments are typecasted to integers
    Raises a TypeError if a or b is a non integer or non float.
    """
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
