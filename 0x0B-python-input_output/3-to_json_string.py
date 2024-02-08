#!/usr/bin/python3
import json
"""
    module that converts an object to json
"""


def to_json_string(my_obj):
    """
        to_json_string: converts my_obj to json string
        my_obj: object to convert
    """

    return (json.dumps(my_obj))
