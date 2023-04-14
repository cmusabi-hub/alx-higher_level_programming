#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    new_dictionary = {}
    if not value:
        return a_dictionary
    for Key, _value in a_dictionary.items():
        if _value != value:
            new_dictionary[Key] = _value
    return new_dictionary
