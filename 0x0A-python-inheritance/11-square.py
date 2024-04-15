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
    """Represents a rectangle"""
    def __init__(self, width, height):
        """Initializes the rectangle"""
        self.integer_validator("width", width)
        self._width = width  
        self.integer_validator("height", height)
        self._height = height  

    def area(self):
        """Calculates the area of the rectangle"""
        return self._width * self._height

    def __str__(self):
        """String representation of the rectangle"""
        return f"[Rectangle] {self._width}/{self._height}"

class Square(Rectangle):
    """Represents a square"""
    def __init__(self, size):
        """Initializes the square"""
        self.integer_validator("size", size)
        self._size = size
        super().__init__(size, size)

    def area(self):
        """Calculates the area of the square"""
        return self._size ** 2

    def __str__(self):
        """String representation of the square"""
        return f"[Square] {self._size}/{self._size}"

