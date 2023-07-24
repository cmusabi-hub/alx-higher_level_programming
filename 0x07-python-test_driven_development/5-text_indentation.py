#!/usr/bin/python3
"""Function definition"""


def text_indentation(text):
    """Function prints 2 new lines after Character signs ., ?, :"""
    char_s = ['.', '?', ':']
    new_char = ""
    index = 0

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for index in range(len(text)):
        new_char += text[index]
        if text[index] in char_s:
            if text[index] != '\n':
                new_char += "\n\n"
    print(new_char.strip())
