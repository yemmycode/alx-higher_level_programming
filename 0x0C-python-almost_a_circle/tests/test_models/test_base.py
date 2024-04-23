#!/usr/bin/python3

"""Unit test suite for base.py."""
import unittest
from models.rectangle import Rectangle
from models.square import Square

class TestBaseCreate(unittest.TestCase):
    """Test cases for the 'create' method in the Base class."""

    def test_rectangle_creation_from_dict(self):
        rect_1 = Rectangle(3, 5, 1, 2, 7)
        dict_of_rect_1 = rect_1.to_dictionary()
        rect_2 = Rectangle.create(**dict_of_rect_1)
        self.assertEqual(str(rect_1), "[Rectangle] (7) 1/2 - 3/5")

    def test_new_rectangle_creation_from_dict(self):
        rect_1 = Rectangle(3, 5, 1, 2, 7)
        dict_of_rect_1 = rect_1.to_dictionary()
        rect_2 = Rectangle.create(**dict_of_rect_1)
        self.assertEqual(str(rect_2), "[Rectangle] (7) 1/2 - 3/5")

    def test_rectangle_identity(self):
        rect_1 = Rectangle(3, 5, 1, 2, 7)
        dict_of_rect_1 = rect_1.to_dictionary()
        rect_2 = Rectangle.create(**dict_of_rect_1)
        self.assertIsNot(rect_1, rect_2)

    def test_rectangle_equality(self):
        rect_1 = Rectangle(3, 5, 1, 2, 7)
        dict_of_rect_1 = rect_1.to_dictionary()
        rect_2 = Rectangle.create(**dict_of_rect_1)
        self.assertNotEqual(rect_1, rect_2)

    def test_square_creation_from_dict(self):
        square_1 = Square(3, 5, 1, 7)
        dict_of_square_1 = square_1.to_dictionary()
        square_2 = Square.create(**dict_of_square_1)
        self.assertEqual(str(square_1), "[Square] (7) 5/1 - 3")

    def test_new_square_creation_from_dict(self):
        square_1 = Square(3, 5, 1, 7)
        dict_of_square_1 = square_1.to_dictionary()
        square_2 = Square.create(**dict_of_square_1)
        self.assertEqual(str(square_2), "[Square] (7) 5/1 - 3")

    def test_square_identity(self):
        square_1 = Square(3, 5, 1, 7)
        dict_of_square_1 = square_1.to_dictionary()
        square_2 = Square.create(**dict_of_square_1)
        self.assertIsNot(square_1, square_2)

    def test_square_equality(self):
        square_1 = Square(3, 5, 1, 7)
        dict_of_square_1 = square_1.to_dictionary()
        square_2 = Square.create(**dict_of_square_1)
        self.assertNotEqual(square_1, square_2)

if __name__ == '__main__':
    unittest.main()

