#!/usr/bin/python3
"""
Contains the class BaseGeometry and subclass Rectangle
"""

class BaseGeometry:
    """Class with public instance methods area and integer_validator"""
    def area(self):
        """Raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """Representation of a rectangle"""
    def __init__(self, width, height):
        """Initializes the rectangle"""
        super().integer_validator("width", width)
        self._width = width
        super().integer_validator("height", height)
        self._height = height

    def area(self):
        """Calculates the area of the rectangle"""
        return self._width * self._height

    def __str__(self):
        """String representation of the rectangle"""
        return f"[Rectangle] {self._width}/{self._height}"
