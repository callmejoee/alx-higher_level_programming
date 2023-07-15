#!/usr/bin/python3
""" This is a text indentation module """


def text_indentation(text):
    """
    puts two blank lines after exclamation marks
    :param text: the string to be scanned
    :return: none
    :raises TypeError: if the string isn't a string
    """
    skip_space = False
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        if skip_space and char == ' ':
            continue
        if char in ('?', '.', ':'):
            print(char, end='')
            print("\n")
            skip_space = True
        else:
            print(char, end='')
            skip_space = False
