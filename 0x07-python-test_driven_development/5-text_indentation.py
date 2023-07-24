#!/usr/bin/python3
"""Function definition"""


def text_indentation(text):
    """Function prints 2 new lines after Character signs ., ?, :"""
    char_s = ['.', '?', ':']
    
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for index in text:
        print(index, end="")
        if index in char_s:
            print('\n')
