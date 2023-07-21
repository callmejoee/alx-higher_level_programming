#!/usr/bin/python3
"""This is the read file"""


def read_file(filename=""):
    """This is a function to read file"""
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end="")
