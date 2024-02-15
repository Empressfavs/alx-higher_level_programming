#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lists = my_list[::-1]
    for i in lists:
        print("{:d}".format(i))
