#!/usr/bin/python3

def remove_char_at(str, n):
    _str = ""
    for i, char_ in enumerate(str):
        if (i == n):
            continue
        else:
            _str += char_
    return(_str)
