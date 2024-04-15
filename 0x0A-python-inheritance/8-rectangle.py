#!/usr/bin/python3
"""
Module with BaseGeometry and its subclass Rectangle.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Defines a rectangle with width and height."""
    def __init__(self, width, height):
        """Initializes the rectangle with width and height."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
