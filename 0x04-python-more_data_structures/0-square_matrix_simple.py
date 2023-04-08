#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = []
    row_matrix = []
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            row_matrix.append(matrix[row][column]**2)
        new_matrix.append(row_matrix)
    return new_matrix
