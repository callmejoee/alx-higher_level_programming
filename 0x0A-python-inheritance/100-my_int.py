#!/usr/bin/python3
""" This is the module for a kind of class """


class MyInt(int):
    """ this is a modded int class """
    def __init__(self, num):
        self.num = num

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
