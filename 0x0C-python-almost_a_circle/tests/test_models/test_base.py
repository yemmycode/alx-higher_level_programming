#!/usr/bin/python3

"""Unit tests for base.py."""
import unittest
from models.rectangle import Rectangle
from models.square import Square

class TestBaseCreate(unittest.TestCase):
    """Tests for the 'create' method of the Base class."""

    def test_create_rectangle_original(self):
        rectangle1 = Rectangle(3, 5, 1, 2, 7)
        rectangle_dict = rectangle1.to_dictionary()
        rectangle2 = Rectangle.create(**rectangle_dict)
        self.assertEqual(str(rectangle1), "[Rectangle] (7) 1/2 - 3/5")

    def test_create_rectangle_new(self):
        rectangle1 = Rectangle(3, 5, 1, 2, 7)
        rectangle_dict = rectangle1.to_dictionary()
        rectangle2 = Rectangle.create(**rectangle_dict)
        self.assertEqual(str(rectangle2), "[Rectangle] (7) 1/2 - 3/5")

    def test_create_rectangle_identity(self):
        rectangle1 = Rectangle(3, 5, 1, 2, 7)
        rectangle_dict = rectangle1.to_dictionary()
        rectangle2 = Rectangle.create(**rectangle_dict)
        self.assertIsNot(rectangle1, rectangle2)

    def test_create_rectangle_equality(self):
        rectangle1 = Rectangle(3, 5, 1, 2, 7)
        rectangle_dict = rectangle1.to_dictionary()
        rectangle2 = Rectangle.create(**rectangle_dict)
        self.assertNotEqual(rectangle1, rectangle2)

    def test_create_square_original(self):
        square1 = Square(3, 5, 1, 7)
        square_dict = square1.to_dictionary()
        square2 = Square.create(**square_dict)
        self.assertEqual(str(square1), "[Square] (7) 5/1 - 3")

    def test_create_square_new(self):
        square1 = Square(3, 5, 1, 7)
        square_dict = square1.to_dictionary()
        square2 = Square.create(**square_dict)
        self.assertEqual(str(square2), "[Square] (7) 5/1 - 3")

    def test_create_square_identity(self):
        square1 = Square(3, 5, 1, 7)
        square_dict = square1.to_dictionary()
        square2 = Square.create(**square_dict)
        self.assertIsNot(square1, square2)

    def test_create_square_equality(self):
        square1 = Square(3, 5, 1, 7)
        square_dict = square1.to_dictionary()
        square2 = Square.create(**square_dict)
        self.assertNotEqual(square1, square2)

if __name__ == '__main__':
    unittest.main()

