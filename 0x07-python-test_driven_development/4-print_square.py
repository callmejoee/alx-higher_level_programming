#!/usr/bin/python3
""" This is a square module """


def print_square(size):
    """
    Function to print a square with the '#' char

    :param size: the size of the square

    :raises TypeError: if the number is not an int
    :raises ValueError: if the number is smaller than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print('#' * size)
