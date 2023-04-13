#!/usr/bin/python3


def weight_average(my_list=[]):
    if not my_list:
        return 0
    ssum = 0
    score = 0
    if my_list:
        for column in my_list:
            mul = column[0] * column[1]
            ssum += mul
            score += column[0]
        average = ssum / score
    return average
