#!/usr/bin/python3

import sys
x = len(sys.argv) - 1
if x < 1:
    print("{} arguments.".format(x))
elif x == 1:
    print("{} argument:".format(x))
else:
    print("{} arguments:".format(x))

for i in range(x):
    print("{}: {:s}".format(i + 1, sys.argv[i + 1]))
