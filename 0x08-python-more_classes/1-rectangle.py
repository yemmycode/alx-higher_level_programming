#!/usr/bin/python3

class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("Width must be greater than or equal to zero.")
        self._width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("Height must be greater than or equal to zero.")
        self._height = value

