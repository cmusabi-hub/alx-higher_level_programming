#!/usr/bin/python3


def uniq_add(my_list=[]):
    return (map(lambda x, y: x + y, list) for list in my_list)
