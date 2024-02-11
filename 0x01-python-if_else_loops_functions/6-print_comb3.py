#!/usr/bin/python3
start = 10
for i in range(start):
    for e in range(i + 1, start):
        print("{:d}{:d}".format(i, e), end=", ")

