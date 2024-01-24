#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self._size = size
        if type(self._size) is not int:
            raise TypeError ("size must be an integer")
        if self._size < 0:
            raise ValueError ("size must be >= 0")
