#!/usr/bin/python3

def no_c(my_string):
    new_string = ""
    for char_l in my_string:
        if (char_l == 'c' or char_l == 'C'):
            continue
        else:
            new_string += char_l
    return (new_string)
