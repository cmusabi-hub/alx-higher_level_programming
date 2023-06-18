#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    for key_dic in list(a_dictionary):
        if key_dic == key:
            a_dictionary[key_dic] = value
        else:
            a_dictionary[key] = value
    return (a_dictionary)
