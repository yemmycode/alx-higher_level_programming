#!/usr/bin/python3
class Rectangle:
    """This class represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with specified width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer.")
        if value < 0:
            raise ValueError("Width must be greater than or equal to zero.")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer.")
        if value < 0:
            raise ValueError("Height must be greater than or equal to zero.")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height) if self.__width and self.__height else 0

    def __str__(self):
        """Return the printable representation of the rectangle."""
        if not self.__width or not self.__height:
            return ""
        return "#" * self.__width + "\n" + ("#" + " " * (self.__width - 2) + "#\n") * (self.__height - 2) + "#" * self.__width + "\n"

    def __repr__(self):
        """Return the string representation of the rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

