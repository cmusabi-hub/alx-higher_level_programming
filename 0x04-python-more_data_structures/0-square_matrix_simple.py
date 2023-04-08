#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            new_matrix.append(matrix[row][column]**2)
    return new_matrix
