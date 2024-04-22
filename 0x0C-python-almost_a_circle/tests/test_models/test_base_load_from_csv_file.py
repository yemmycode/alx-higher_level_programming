#!/usr/bin/python3

"""Unit tests for the base.py module."""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseLoadFromCSV(unittest.TestCase):
    """Tests for the 'load_from_file_csv' method of the Base class."""

    @classmethod
    def tearDownClass(cls):
        """Remove CSV files after tests."""
        try:
            os.remove("Rectangle.csv")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.csv")
        except FileNotFoundError:
            pass

    def test_loading_first_rectangle_from_csv(self):
        rectangle1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file_csv([rectangle1])
        rectangles = Rectangle.load_from_file_csv()
        self.assertEqual(str(rectangle1), str(rectangles[0]))

    def test_loading_second_rectangle_from_csv(self):
        rectangle1 = Rectangle(10, 7, 2, 8, 1)
        rectangle2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rectangle1, rectangle2])
        rectangles = Rectangle.load_from_file_csv()
        self.assertEqual(str(rectangle2), str(rectangles[1]))

    def test_rectangle_type_after_loading_from_csv(self):
        rectangle1 = Rectangle(10, 7, 2, 8, 1)
        rectangle2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rectangle1, rectangle2])
        rectangles = Rectangle.load_from_file_csv()
        self.assertTrue(all(isinstance(obj, Rectangle) for obj in rectangles))

    def test_loading_first_square_from_csv(self):
        square1 = Square(5, 1, 3, 3)
        Square.save_to_file_csv([square1])
        squares = Square.load_from_file_csv()
        self.assertEqual(str(square1), str(squares[0]))

    def test_loading_second_square_from_csv(self):
        square1 = Square(5, 1, 3, 3)
        square2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([square1, square2])
        squares = Square.load_from_file_csv()
        self.assertEqual(str(square2), str(squares[1]))

    def test_square_type_after_loading_from_csv(self):
        square1 = Square(5, 1, 3, 3)
        square2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([square1, square2])
        squares = Square.load_from_file_csv()
        self.assertTrue(all(isinstance(obj, Square) for obj in squares))

    def test_loading_from_csv_when_no_file_exists(self):
        squares = Square.load_from_file_csv()
        self.assertEqual(squares, [])

    def test_loading_from_csv_with_incorrect_arguments(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)

if __name__ == "__main__":
    unittest.main()

