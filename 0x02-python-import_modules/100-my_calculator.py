#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv


def main():
    operator = {'+': add, '-': sub, '*': mul, '/': div}


    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        op = argv[2]
        b = int(argv[3])
        
        if op not in operator:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            result = operator[op](a, b)
            print("{} {} {} = {}".format(a, op, b, result))


if __name__ == "__main__":
    main()
