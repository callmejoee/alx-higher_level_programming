#!/usr/bin/python3
""" This is the rectangle module """


class Rectangle:
    """
    rectangle class

    Attributes:
    __height (int): height of the rectangle
    __width (int): width of rectangle
    number_of_instances (int): number of class instances that are available
    print_symbol (char): the char the rect is drawn with

    Methods:
    area(): prints the area
    """
    number_of_instances = 0
    print_symbol = '#'

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
            Rectangle.number_of_instances += 1

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
        if self.width and self.height:
            return 2 * (self.width + self.height)
        else:
            return 0

    def __str__(self):
        rectangle = ""
        for i in range(self.height):
            rectangle += print_symbol * self.width
            if i != self.height - 1 and self.width != 0:
                rectangle += '\n'
        return rectangle

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
