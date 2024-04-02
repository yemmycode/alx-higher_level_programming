#!/usr/bin/python3

"""Definition of the Square class."""

class Square:
    """Representation of a square."""

    def __init__(self, size):
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
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self._size ** 2

    def my_print(self):
        """Print the square with the '#' character."""
        for _ in range(self._size):
            print("#" * self._size)
        if self._size == 0:
            print()
