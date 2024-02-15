#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    lists = my_list[::-1]
    for i in lists:
        print("{:d}".format(i))
