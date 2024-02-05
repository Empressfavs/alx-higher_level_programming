#!/usr/bin/python3
"""
MyList: A subclass that inherits list
"""


class MyList(list):
    """
    print_sorted: prints the list in ascending order (sorted)
    """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
