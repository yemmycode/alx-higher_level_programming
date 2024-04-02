#!/usr/bin/python3

"""
This module defines a class called Square.
"""


class Square:
    """
    Represents a square.

    Attributes:
        size (int): The size of the new square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
