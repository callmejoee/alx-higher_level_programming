#!/usr/bin/python3
"""This is the file"""


def write_file(filename="", text=""):
    """This is a function to write file"""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
