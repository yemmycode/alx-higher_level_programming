#!/usr/bin/python3
"""
Function to read a UTF8 text file and output its contents to the console.
"""


def read_file(filename=""):
    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read(), end='')
