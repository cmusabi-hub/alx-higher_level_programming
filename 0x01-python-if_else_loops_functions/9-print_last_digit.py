#!/usr/bin/python3

def print_last_digit(number):
    number = str(number)
    for i in number:
        result = i[-1]
    print("{}".format(result), end="")
