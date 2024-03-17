#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        for i in range(len(my_list)):
            list = my_list[len(my_list) - i - 1]
            print("{:d}".format(list))
