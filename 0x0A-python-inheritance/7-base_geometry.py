#!/usr/bin/python3
"""
Module including the BaseGeometry class.
"""

class BaseGeometry:
    """Defines methods for geometric calculations."""
    def area(self):
        """Notifies that the area calculation is not available."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Ensures the provided value is a positive integer."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
