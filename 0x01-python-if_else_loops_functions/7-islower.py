#!/usr/bin/python3

def islower(c):
    test = ord(c)
    if  test in range(ord('a'), (ord('z') + 1)):
        return(True)
    else:
        return(False)
