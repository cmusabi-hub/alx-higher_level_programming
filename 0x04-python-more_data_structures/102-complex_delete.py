#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    new_dictionary = {}
    for Key, _value in a_dictionary.items():
        if _value == value:
            del a_dictionary[Key]
        new_dictionary = a_dictionary[Key]
    return new_dictionary
