#!/usr/bin/python3
"""
add_integer: adds a and b together
"""


def add_integer(a, b=98):
    """
    add_integer: a function that adds the value of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a + b)
