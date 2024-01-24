#!/usr/bin/python3
"""
class Square: a class Square that defines a square
"""


class Square:
    """
    A square class that shows private instance attribute: size
    """
    def __init__(self, size=0):
        """
        size: The size of the instance attribute
        """
        self._square__size = size
        if type(self._square__size) is not int:
            raise TypeError("size must be an integer")
        if self._square__size < 0:
            raise ValueError("size must be >= 0")
