#!/usr/bin/python3
def no_c(my_string):
    list = ""
    for i in my_string:
        if i == "c" or i == "C":
            continue

        list += i
    return list
