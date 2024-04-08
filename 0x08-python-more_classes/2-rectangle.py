#!/usr/bin/python3
class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer.")
        if value < 0:
            raise ValueError("Width must be >= 0.")
        self._width = value

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer.")
        if value < 0:
            raise ValueError("Height must be >= 0.")
        self._height = value

    def area(self):
        """Return the area of the rectangle."""
        return self._width * self._height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return (self._width + self._height) * 2 if self._width and self._height else 0
