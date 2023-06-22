#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    total_elements = 0
    for element in range(x):
        try:
            print("{:d}".format(my_list[element]), end="")
            total_elements += 1
        except (ValueError, TypeError):
            continue
    return (total_elements)
