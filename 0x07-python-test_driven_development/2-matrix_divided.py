#!/usr/bin/python3
"""Function that divides elements of a matrix"""


def matrix_divided(matrix, div):
    """Function matrtix"""
    if not all(isinstance(row, list) and all(
               isinstance(element, (int, float)) for element in row)
               for row in matrix):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    len_row = set(len(row) for row in matrix)
    if len(len_row) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if (div == 0):
        raise ZeroDivisionError("division by zero")

    new_matrix = list(map(lambda row:
                          (list(map(lambda column: round
                                    (column / div, 2), row))), matrix))

    return (new_matrix)
