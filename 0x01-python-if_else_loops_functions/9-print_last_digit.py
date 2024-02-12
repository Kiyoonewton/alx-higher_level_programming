#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        num = number * -1
    else:
        num = number
    print("{}".format(num % 10), end="")
