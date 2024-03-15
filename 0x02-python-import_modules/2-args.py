#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    num_arguments = len(argv) - 1

    if num_arguments < 1:
        print("{} argument.".format(num_arguments))
    elif num_arguments == 1:
        print("{} argument:".format(num_arguments))
    else:
        print("{} arguments:".format(num_arguments))

    for i in range(num_arguments):
        print("{}: {}".format(i + 1, argv[i + 1]))
