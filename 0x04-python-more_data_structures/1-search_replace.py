#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    for row in my_list:
        if (row == search):
            row = replace
        new_list.append(row)
    return (new_list)
