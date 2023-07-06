#!/usr/bin/python3
""" This is the rectangle module """


class Rectangle:
    """
    rectangle class

    Attributes:
    __height (int): height of the rectangle
    __width (int): width of rectangle

    Methods:
    area(): prints the area
    perimeter(): prints the permieter

    """

    def __init__(self, width=0, height=0):
        """
                initializes a new rectangle with default size of 0

                Args:
                width,height (int): width and height zero default


                Raises:
                ValueError: if width or height is negative
                TypeError: if not integer

        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width > 0 and self.height > 0:
            return 2 * (self.width + self.height)
        else:
            return 0
