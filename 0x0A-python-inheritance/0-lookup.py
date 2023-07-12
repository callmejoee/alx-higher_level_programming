#!/usr/bin/python3

"""
This is a module that provides a function to find the method of object
"""
def lookup(obj):
    """
    prints all methods and arguments

    Args: obj (obj): object
    returns: list
    """
    return(dir(obj))
