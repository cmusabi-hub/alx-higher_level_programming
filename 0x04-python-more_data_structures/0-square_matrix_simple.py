#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_list = []
    for row in matrix:
        new_list2 = []
        for column in row:
            new_list2.append(column ** 2)
        new_list.append(new_list2)
    return (new_list)
