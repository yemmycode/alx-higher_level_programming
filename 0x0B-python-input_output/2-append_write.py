#!/usr/bin/python3
"""Module for appending text to a file.
Function to add a string to the end of a text file.
"""


def append_write(filename="", text=""):
    """Function to append a string to the end of a text file.
    Parameters:
        filename (str): The file to which the text will be appended.
        text (str): The string to append to the file.
    Returns:
        int: The number of characters appended.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
