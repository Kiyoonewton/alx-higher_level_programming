#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        if len(i) > 0:
            for x in i:
                if i.index(x) < len(i) - 1:
                    print("{:d}".format(x), end=" ")
                else:
                    print("{:d}".format(x))
        else: 
            print("")
