#!/usr/bin/python3
def uppercase(str):
    for _char in str:
        if ord(_char) in range(97, 127):
            print(chr(ord(_char) - 32), end='')
        else:
            print(_char, end='')
    print()


