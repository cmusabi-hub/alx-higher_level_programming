#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    for key_dic in list(a_dictionary):
        if key_dic == key:
            del(a_dictionary[key_dic])
    return (a_dictionary)
