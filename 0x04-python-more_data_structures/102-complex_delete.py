#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    if not value:
        return a_dictionary
    for Key in list(a_dictionary):
        if a_dictionary[Key] == value:
            del a_dictionary[Key]
    return a_dictionary
