#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        divide_nums = a / b
    except (ZeroDivisionError, TypeError):
        divide_nums = None
    finally:
        print("Inside result:".format(divide_nums))
    return (divide_nums)
