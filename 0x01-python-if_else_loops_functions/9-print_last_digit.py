#!/usr/bin/python3

def print_last_digit(number):
    mod_num = ((number % 10) if number >= 0 else (number * -1) % 10)
    print(mod_num, end="")
    return mod_num
