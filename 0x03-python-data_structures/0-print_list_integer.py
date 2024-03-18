#!/usr/bin/python3

def print_list_integer(my_list=[]):
    for item in my_list:
        if isinstance(item, int):
            print("{:d}".format(item))

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
