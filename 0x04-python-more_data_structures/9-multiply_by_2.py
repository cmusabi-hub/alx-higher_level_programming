#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for Key, Values in a_dictionary.items():
        new_dictionary[Key] = Values * 2
    return new_dictionary
