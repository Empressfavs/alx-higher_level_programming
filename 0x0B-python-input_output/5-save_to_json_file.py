#!/usr/bin/python3
"""
save_to_json_file: a function that writes an Object to a text file,
using a JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """
    a function that writes an Object to a text file,
    using a JSON representation
    """
    with open("my_obj", mode="w", encoding="utf-8") as file:
        return json.dump(my_obj, file)
