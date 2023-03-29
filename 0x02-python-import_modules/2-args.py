#!/usr/bin/python3
from sys import argv

def main():
    argument  = len(argv) - 1
    if argument == 0:
           print("0 arguments.")
    elif argument == 1:
        print("1 argument:")
        print("{}: {}".format(argument, argv[argument]))
    else:
        print("{} arguments:".format(argument))
        for i in range(1, argument + 1):
            print("{} : {}".format(i, argv[i]))
if __name__ == "__main__":
    main()
