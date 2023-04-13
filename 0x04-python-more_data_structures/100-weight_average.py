#!/usr/bin/python3


def weight_average(my_list=[]):
    if not my_list:
        return 0
    total_weight = 0
    total_score = 0
    if my_list:
        for score, weight in my_list:
            total_weight += score * weight 
            total_score += score
        average = total_weight / total_score
    return average
