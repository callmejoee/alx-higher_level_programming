#!/usr/bin/python3
""" This is the module for a kind of class """


def inherits_from(obj, a_class):
    """ Function to check if subclass """
    return issubclass(type(obj), a_class) and type(obj) != a_class
