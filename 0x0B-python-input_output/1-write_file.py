#!/usr/bin/python3
"""
Function to write a string to a UTF8-encoded text file and return the character count.
"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
