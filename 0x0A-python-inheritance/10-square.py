#!/usr/bin/python3
"""
Contains the class BaseGeometry and subclass Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Class representing a square"""
    def __init__(self, size):
        """Initializes the square"""
        self.integer_validator("size", size)
        self._size = size  # Protected attribute
        super().__init__(size, size)

    def area(self):
        """Calculates the area of the square"""
        return self._size ** 2

    def __str__(self):
        """String representation of the square"""
        return f"[Square] {self._size}/{self._size}"
