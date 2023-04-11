#!/usr/bin/python3


def best_score(a_dictionary):
    max = a_dictionary[0]
    if len(a_dictionary) == "":
        return None
    for i in len(a_dictionary.items()):
        if max < a_dictionary[i]:
            max = a_dictionary[i]
    return max
