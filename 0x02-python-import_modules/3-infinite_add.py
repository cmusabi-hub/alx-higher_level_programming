#!/usr/bin/python3
from sys import argv


def main():
    sum = 0
    if (len(argv) > 1):
        for i in range(1, len(argv)):
            sum += int(argv[i])
        print("{}".format(sum))
    else:
        print("{}".format(sum))


if __name__ == "__main__":
    main()
