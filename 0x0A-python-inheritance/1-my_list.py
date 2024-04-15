#!/usr/bin/python3
"""Module for custom list manipulation."""

class MyList(list):
    """A subclass of the built-in list type."""
    def print_sorted(self):
        """Display the elements of the list in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
