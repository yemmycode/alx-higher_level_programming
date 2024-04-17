#!/usr/bin/python3
"""Module for appending text after a specific string in a file."""

def append_after(filename="", search_string="", new_string=""):
    """Inserts new_string after each line containing search_string.
    Args:
        - filename: The name of the file
        - search_string: The string to search for within the file
        - new_string: The string to insert after the search_string
    """
    lines = []
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
