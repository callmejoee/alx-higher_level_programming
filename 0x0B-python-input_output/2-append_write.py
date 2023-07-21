#!/usr/bin/python3
"""This is the file"""


def append_write(filename="", text=""):
    """This is a function to append file"""
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
