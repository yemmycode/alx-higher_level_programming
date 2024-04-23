#!/usr/bin/python3
"""
A module defining a square class.
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    A class to represent a square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Construct a new instance of Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieve or set the square's size."""
        return self.width

    @size.setter
    def size(self, value):
        if isinstance(value, int) and value > 0:
            self.width = self.height = value

    def update(self, *args, **kwargs):
        """
        Assign new values to the square's attributes.
        """
        attrs = ['id', 'size', 'x', 'y']
        # Using args
        for attr, arg in zip(attrs, args):
            setattr(self, attr, arg) if arg else None
        # Using kwargs
        for attr in attrs:
            if attr in kwargs:
                setattr(self, attr, kwargs[attr])

    def to_dictionary(self):
        """Provide the square's dictionary representation."""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

    def __str__(self):
        """Generate the string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

