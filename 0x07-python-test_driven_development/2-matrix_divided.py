#!/usr/bin/python3
"""Function that divides elements of a matrix"""


def matrix_divided(matrix, div):
    """Function matrtix"""
    new_matrix = []

    if not all(isinstance(row, list) and all(
        isinstance(element, (int, float)) for element in row) for row in matrix):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    len_row = set(len(row) for row in matrix)
    if len_row > 1:
        raise TypeError("Each row of the matrix must have the same size")
