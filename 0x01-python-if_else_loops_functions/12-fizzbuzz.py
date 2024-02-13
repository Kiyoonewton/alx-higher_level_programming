#!/usr/bin/python3
def fizzbuzz():
    for index in range(1, 101):
        if (index % 5 == 0 and index % 3 == 0):
            print("{}".format("FizzBuzz"), end=" ")
        elif (index % 5 == 0):
            print("{}".format("Buzz"), end=" ")
        elif (index % 3 == 0):
            print("{}".format("Fizz"), end=" ")
        else:
            print("{}".format(index), end=" ")
