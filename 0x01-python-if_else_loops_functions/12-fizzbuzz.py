#!/usr/bin/python3

def fizzbuzz():
    for n in range(1, 101):
        output = ""
        if n % 3 == 0:
            output += "Fizz"
        if n % 5 == 0:
            output += "Buzz"
        if output:
            print(output, end=" ")
        else:
            print("{} ".format(n), end="")

fizzbuzz()

