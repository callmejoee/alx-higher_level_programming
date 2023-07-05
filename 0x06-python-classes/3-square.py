#!/usr/bin/python3
""" This is the square module """


class Square:
    """
    square class

    Attributes:
    __size (int): size of the square

    Methods:
    area(): prints the area
    """

    def __init__(self, size=0):
        """
        initializes a new square with default size of 0

        Args:
        size (int): size zero default

        Raises:
        ValueError: if size is negative
        TypeError: if not integer

        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ Calulates area
        Returns:
        int: area of square
        """
        return self.__size*self.__size
