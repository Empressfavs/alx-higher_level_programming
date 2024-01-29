#!/usr/bin/python3
"""
class Square: a class Square that defines a square
"""


class Square:
    """
    A square class that shows private instance attribute
    """

    def __init__(self, size=0):
        """
        __init__: Initializes a Square object
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        area: calculates the area of the square
        """
        return self.__size ** 2
