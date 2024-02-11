#!/usr/bin/python3
start = 97
for i in range(start, start + 26):
    if(i == 113 or i==101):
        pass
    else: print("{:c}".format(i), end="")
