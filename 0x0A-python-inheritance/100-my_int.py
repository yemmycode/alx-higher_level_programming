#!/usr/bin/python3
"""
Contains the class MyInt
"""

class MyInt(int):
    """A rebel version of an integer, perfect for opposite day!"""
    def __new__(cls, *args, **kwargs):
        """Creates a new instance of the class"""
        return super().__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """Inverts the equality operation"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """Inverts the inequality operation"""
        return not super().__ne__(other)
