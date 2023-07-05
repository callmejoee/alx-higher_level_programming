#!/usr/bin/python3
""" This is the square module """


class Square:
    """
    square class

    Attributes:
    __size (int): size of the square
    __position (tuple):
    Methods:
    area(): prints the area
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        initializes a new square with default size of 0

        Args:
        size (int): size zero default
        position (tuple): zero default

        Raises:
        ValueError: if size is negative
        TypeError: if not integer
        TypeError: if not tuple of size 2

        """
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.__position = position

    def area(self):
        """ Calculates area
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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, pos):
        if not isinstance(self.__position, tuple) or len(tuple) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = pos

    def my_print(self):
        """
        function to display the square
        """
        if self.size > 0:
            for i in range(self.size):
                if self.position[1] >= 0:
                    print("_" * self.position[0], end="")
                for j in range(self.size):
                    print("#", end="")
                print()
        else:
            print()
