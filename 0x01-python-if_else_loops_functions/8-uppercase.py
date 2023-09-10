#!/usr/bin/python3

def uppercase(str):
    letters = ''
    for letter in str:
        if ord(letter) in range(ord('a'), ord('z')):
            letters += chr(ord(letter) - 32)
        else:
            letters += letter
    print("{:s}".format(letters))
