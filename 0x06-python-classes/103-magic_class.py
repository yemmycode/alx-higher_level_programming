#!/usr/bin/python3

"""MagicClass definition matching the given bytecode."""

import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize a MagicClass.

        Args:
            radius (int or float): The radius of the new MagicClass.
        """
        self._MagicClass__radius = 0
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """Calculate the area of the MagicClass."""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """Calculate the circumference of the MagicClass."""
        return 2 * math.pi * self._MagicClass__radius
