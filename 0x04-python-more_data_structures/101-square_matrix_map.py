#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    return(list(map(lambda row: list(map(lambda column: column ** 2, row)), matrix)))
