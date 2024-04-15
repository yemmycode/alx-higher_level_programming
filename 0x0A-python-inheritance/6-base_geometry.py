#!/usr/bin/python3
"""
Module defining BaseGeometry class.
"""

class BaseGeometry:
    """Class that defines a geometric shape with an unimplemented area."""
    def area(self):
        """Raises a NotImplementedError if method is not defined in subclass."""
        raise NotImplementedError("area() is not implemented")
