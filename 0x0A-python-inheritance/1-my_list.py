#!/usr/bin/python3
"""This is a module that contains class Mylist"""


class MyList(list):
    """
    Child class for list
    """
    def __init__(self):
        """ initializes the super class """
        super().__init__()

    def append(self, item):
        """Appends to the list"""
        super().append(int(item))

    def print_sorted(self):
        """Prints the sorted list"""
        self.sort()
        print(self)
