#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for key_dic, values_dic in sorted(a_dictionary.items()):
        print("{0:s}: {1:}".format(key_dic, values_dic))
