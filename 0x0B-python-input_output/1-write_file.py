#!/usr/bin/python3
"""
write_file: checks the length of a text file
"""


def write_file(filename="", text=""):
    """
    a function that writes a string to a text file (UTF8)
    and returns the number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as newfile:
        return (newfile.write(text))
