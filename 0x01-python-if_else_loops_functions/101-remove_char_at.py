#!/usr/bin/python3

def remove_char_at(str, n):
    _str = ""
    num = 0
    for charc in str:
        if num != n:
            _str += charc
        num += 1
    return(_str)
