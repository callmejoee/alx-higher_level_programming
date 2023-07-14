#!/usr/bin/python3
""" This is a module for the add function """


def add_integer(a, b=98):
    """ This is the add function """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
