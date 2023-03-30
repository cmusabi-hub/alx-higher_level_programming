#!/usr/bin/python3


def main():
    from sys import argv
    from calculator_1 import add, sub, mul, div

    operator = {"+":"add", "-":"sub", "-":"mul", "/":"div"}
    argument = len(argv) - 1
    a = int(argv[1])
    b = int(argv[3])

    if argument <= 2:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] not in list(operator.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
    else:
        print("{} {} {} = {}".format(a, argv[2], b, operator[argv[2]](a, b)))


if __name__ == "__main__":
    main()
