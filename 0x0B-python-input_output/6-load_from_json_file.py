#!/usr/bin/python3
"""
load_from_json_file: a function that creates an Object
from a “JSON file”
"""


import json


def load_from_json_file(filename):
    """
    a function that creates an Object from a “JSON file”
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        json.load(file)
