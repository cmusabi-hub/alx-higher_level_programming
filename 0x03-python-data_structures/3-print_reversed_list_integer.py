#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for i in reversed(my_list):
        if (my_list == []):
            return(None)
        else:
            print("{:d}".format(i))
