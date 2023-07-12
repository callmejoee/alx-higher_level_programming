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


class Rectangle(BaseGeometry):
    """A derived class rectangle"""
    def __init__(self, width, height):
        """instantiation of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

class Square(Rectangle):
    """This is a derived class from rectangle """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Overridden function"""
        return self.__size ** 2
