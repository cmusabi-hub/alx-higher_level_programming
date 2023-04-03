#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    newlist = []
    for i in my_list:
        newlist.append(i)
        if (my_list[idx]):
            newlist.append = element
        return newlist
        elif idx < 0 or idx > (len(my_list) - 1):
            return my_list
