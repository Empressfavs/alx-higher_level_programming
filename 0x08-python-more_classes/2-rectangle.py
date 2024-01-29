#!/usr/bin/python3
"""
class Rectangle: defines empty class
"""


class Rectangle:
    """
    A rectangle class that shows private instance attribute
    """
    def __init__(self, width=0, height=0):
        """
        __init__: Initializes a Square object
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        my_perimeter = 2 * (self.width + self.height)
        if self.width == 0 or self.height == 0:
            my_perimeter = 0
        else:
            return my_perimeter
