#!/usr/bin/python3
"""
append_write: appends text to a file
"""


def append_write(filename="", text=""):
    """
    a function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as newfile:
        return newfile.write(text)
