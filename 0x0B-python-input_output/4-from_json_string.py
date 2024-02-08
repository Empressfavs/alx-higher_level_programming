#!/usr/bin/python3
import json
"""
from_json_string: a function that returns the
JSON representation of an object (string)
"""


def from_json_string(my_str):
    """
    a function that returns the JSON representation of an object (string)
    """
    return json.loads(my_str)
