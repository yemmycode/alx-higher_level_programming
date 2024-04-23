#!/usr/bin/python3
"""
Module representing a Rectangle.
"""
from models.base import Base


class Rectangle(Base):
    """
    Class representing a Rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Compute the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle using '#' characters."""
        print("\n" * self.y + "\n".join(" " * self.x + "#" * self.width for _ in range(self.height)))

    def __str__(self):
        """Return string representation of the Rectangle instance."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update the attributes of the Rectangle instance."""
        if args:
            for count, arg in enumerate(args):
                setattr(self, ['id', 'width', 'height', 'x', 'y'][count], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the Rectangle instance."""
        return {'id': self.id, 'width': self.width, 'height': self.height, 'x': self.x, 'y': self.y}


if __name__ == "__main__":
    pass

