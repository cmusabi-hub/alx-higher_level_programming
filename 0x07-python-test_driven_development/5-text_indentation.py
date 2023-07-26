#!/usr/bin/python3
"""Function definition"""


def text_indentation(text):
    """Function prints 2 new lines after Character signs ., ?, :"""
    char_s = ['.', '?', ':']
    new_char = ""
    final_char = ""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for index in range(len(text)):
        new_char += text[index]

        if text[index] == "\n":
            final_char += new_char + '\n'
        elif text[index] in char_s:
            new_char = new_char.strip()
            final_char += new_char + "\n\n"
            new_char = ""

    new_char = new_char.strip()
    final_char += new_char

    print(final_char, end="")
