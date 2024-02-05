#!/usr/bin/python3
"""
is_same_class: returns true if an object is the same as the specified class
"""


def is_same_class(obj, a_class):
    """
     a function that returns True if the object is exactly an instance a class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
