#!/usr/bin/python3
"""
Base: The object of a class
"""


class Base:
    """
    A class base that takes value arguments
    """
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
