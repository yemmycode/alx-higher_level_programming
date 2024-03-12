#!/usr/bin/python3

for i in range(100):
    if i is 99:
        print("{}".format(i))
    else:
        print("{:02d}, ".format(i), end='')
