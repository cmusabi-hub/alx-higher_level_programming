#!/usr/bin/python3


def uniq_add(my_list=[]):
    new_list = []
    for list in range(len(my_list)):
        if my_list[list] not in new_list:
            new_list.append(my_list[list])
        else:
            continue
    return (map(lambda x, y: x + y, list) for list in new_list)
