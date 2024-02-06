#!/usr/bin/python3
"""
read_file: reads file in the .txt file"
"""


def read_file(filename=""):
    """
    a function that reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, mode="r", encoding="utf-8") as newfile:
        print(newfile.read(), end="")
