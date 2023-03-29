#!/usr/bin/python3
from sys import argv

def main():
    sum = 0
    argument = len(argv) - 1
    if argument == 0:
        print("0")
    else:
        for num in range(1, argument + 1):
            sum = sum + int(argv[num])
        print(sum)


if __name__ == "__main__":
    main()
