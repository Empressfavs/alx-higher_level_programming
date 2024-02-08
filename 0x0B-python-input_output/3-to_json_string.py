#!/usr/bin/python3
"""
    module that converts an object to json
"""


import json


def to_json_string(my_obj):
    """
        converts my_obj to json string
        my_obj: object to convert
    """

    return (json.dumps(my_obj))
