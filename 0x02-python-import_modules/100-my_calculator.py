#!/usr/bin/python3


def main():
    from sys import argv
    from calculator_1 import add, sub, mul, div

    sign = {"+": add, "-": sub, "*": mul, "/": div}
    argument = len(argv) - 1

    if argument != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] not in sign:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        result = sign[argv[2]](a, b)
        print("{} {} {} = {}".format(a, argv[2], b, result))


if __name__ == "__main__":
    main()
