#!/usr/bin/python3

"""Unit tests for the base.py file."""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseLoadFromFile(unittest.TestCase):
    """Tests for the 'load_from_file' method in the Base class."""

    @classmethod
    def tearDownClass(cls):
        """Remove files created during the tests."""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

    def test_loading_first_rectangle_from_file(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rect1, rect2])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(str(rectangles[0]), str(rect1))

    def test_loading_second_rectangle_from_file(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rect1, rect2])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(str(rectangles[1]), str(rect2))

    def test_rectangle_type_after_loading_from_file(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rect1, rect2])
        rectangles = Rectangle.load_from_file()
        self.assertTrue(all(isinstance(obj, Rectangle) for obj in rectangles))

    def test_loading_first_square_from_file(self):
        square1 = Square(5, 1, 3, 3)
        square2 = Square(9, 5, 2, 3)
        Square.save_to_file([square1, square2])
        squares = Square.load_from_file()
        self.assertEqual(str(squares[0]), str(square1))

    def test_loading_second_square_from_file(self):
        square1 = Square(5, 1, 3, 3)
        square2 = Square(9, 5, 2, 3)
        Square.save_to_file([square1, square2])
        squares = Square.load_from_file()
        self.assertEqual(str(squares[1]), str(square2))

    def test_square_type_after_loading_from_file(self):
        square1 = Square(5, 1, 3, 3)
        square2 = Square(9, 5, 2, 3)
        Square.save_to_file([square1, square2])
        squares = Square.load_from_file()
        self.assertTrue(all(isinstance(obj, Square) for obj in squares))

    def test_loading_from_file_when_no_file_exists(self):
        squares = Square.load_from_file()
        self.assertEqual(squares, [])

    def test_loading_from_file_with_incorrect_arguments(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)

if __name__ == "__main__":
    unittest.main()

