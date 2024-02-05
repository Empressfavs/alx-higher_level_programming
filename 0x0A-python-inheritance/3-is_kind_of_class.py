#!/usr/bin/python3
"""
is_kind_of_class: a function that returns true
"""


def is_kind_of_class(obj, a_class):
    """
    if the object is an instance of a class inherited from the specified class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
