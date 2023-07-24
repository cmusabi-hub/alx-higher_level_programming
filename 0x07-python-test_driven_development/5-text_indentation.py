#!/usr/bin/python3
"""Function definition"""


def text_indentation(text):
    """Function prints 2 new lines after Character signs ., ?, :"""
    char_s = ['.', '?', ':']
    new_char = ""
    
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for index in text:
        new_char += index
        if index in char_s:
            new_char += "\n\n"
    print(new_char.strip())
