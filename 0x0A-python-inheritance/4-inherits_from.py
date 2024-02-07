#!/usr/bin/python3
"""
inherits_from: a function that returns True or False
"""


def inherits_from(obj, a_class):
    """
    a function that returns True if the object is an instance of a clas
    that inherited from the specified class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
