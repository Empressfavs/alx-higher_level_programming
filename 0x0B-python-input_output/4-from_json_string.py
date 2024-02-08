#!/usr/bin/python3
"""
from_json_string: a function that returns the
JSON representation of an object (string)
"""


import json


def from_json_string(my_str):
    """
    a function that returns the JSON representation of an object (string)
    """
    return json.loads(my_str)
