#!/usr/bin/python3
""" This is the module for a kind of class """


class BaseGeometry:
    """ empty class """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates that value is an integer greater than 0 and is int """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
