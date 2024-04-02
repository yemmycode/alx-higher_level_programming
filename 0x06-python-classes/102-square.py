#!/usr/bin/python3

"""Square class definition."""

class Square:
    """Representation of a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self._size = size

    @property
    def size(self):
        """Get or set the current size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """Return the current area of the square."""
        return self._size * self._size

    def __eq__(self, other):
        """Define the == comparison to another square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to another square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to another square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to another square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to another square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= comparison to another square."""
        return self.area() >= other.area()
