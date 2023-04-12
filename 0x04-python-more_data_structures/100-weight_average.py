#!/usr/bin/python3


def weight_average(my_list=[]):
    return (map(lambda score, weight: (score * weight)/, sset[0], sset[1]) for sset in my_list)
