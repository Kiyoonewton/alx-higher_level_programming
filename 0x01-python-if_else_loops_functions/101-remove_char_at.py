#!/usr/bin/python3
def remove_char_at(str, n):
    if (n < 0):
        str_remove = str
    else:
        str_remove = str[0:n] + str[n + 1:]
    return str_remove
