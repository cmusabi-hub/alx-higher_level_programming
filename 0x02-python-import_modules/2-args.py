#!/usr/bin/python3


from sys import argv


def main():
    print("{} arguments:".format(len(argv) - 1))
    for i in range(1, len(argv)):
        print("{:d}: {}".format(i, argv[i]))


if __name__ == "__main__":
    main()
