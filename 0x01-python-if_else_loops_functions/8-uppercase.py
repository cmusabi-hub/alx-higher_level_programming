#!/usr/bin/python3
def uppercase(str):
    result = ""
    for _char in str:
        if ord(_char) in range(97, 127):
            result += chr(ord(_char) - 32)
        else:
            result += _char
    print("{}".format(result))
