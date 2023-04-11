#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    test = list(a_dictionary)[0]
    max = a_dictionary[test]
    for Key, Value in a_dictionary.items():
        if Value > max:
            max = Value
            test = Key
    return test
