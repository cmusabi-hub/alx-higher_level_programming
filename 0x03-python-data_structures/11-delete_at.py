#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    """ Delete value of a list at an index """
    if idx < 0 | idx > len(my_list):
        return my_list
    else:
        del my_list[idx]
    return my_list
