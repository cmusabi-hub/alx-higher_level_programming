#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list == []:
        return (0)
    total_weight = 0
    total_score = 0
    for row in my_list:
        total_weight += (row[0] * row[1])
        total_score += row[1]
    average = total_weight / total_score
    return (average)
