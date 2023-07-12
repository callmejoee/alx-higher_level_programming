#!/usr/bin/python3
""" This is the module for a kind of class """


class BaseGeometry:
    """ empty class """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
