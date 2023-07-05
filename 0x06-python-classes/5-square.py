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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Calulates area
        Returns:
        int: area of square
        """
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        function to display the square
        """
        if self.size > 0:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print()
        else:
            print()
