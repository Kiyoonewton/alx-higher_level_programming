#!/usr/bin/python3
start = 10
for i in range(start):
    for e in range(i + 1, start):
        if (i == 8):
            print("{:d}{:d}".format(i, e))
            break
        print("{:d}{:d}".format(i, e), end=", ")
