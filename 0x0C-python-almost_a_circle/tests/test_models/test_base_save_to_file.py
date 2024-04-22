#!/usr/bin/python3

"""Unit tests for the base.py file."""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseSaveToFile(unittest.TestCase):
    """Tests for the 'save_to_file' method in the Base class."""

    @classmethod
    def tearDownClass(cls):
        """Clean up files after tests."""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass
        try:
            os.remove("Base.json")
        except FileNotFoundError:
            pass

    def test_saving_single_rectangle_to_file(self):
        rectangle = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([rectangle])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 53)

    def test_saving_multiple_rectangles_to_file(self):
        rect1 = Rectangle(10, 7, 2, 8, 5)
        rect2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([rect1, rect2])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 105)

    def test_saving_single_square_to_file(self):
        square = Square(10, 7, 2, 8)
        Square.save_to_file([square])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 39)

    def test_saving_multiple_squares_to_file(self):
        square1 = Square(10, 7, 2, 8)
        square2 = Square(8, 1, 2, 3)
        Square.save_to_file([square1, square2])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 77)

    def test_filename_from_class_name_in_save_to_file(self):
        square = Square(10, 7, 2, 8)
        Base.save_to_file([square])
        with open("Base.json", "r") as file:
            self.assertTrue(len(file.read()) == 39)

    def test_overwriting_file_in_save_to_file(self):
        square = Square(9, 2, 39, 2)
        Square.save_to_file([square])
        square = Square(10, 7, 2, 8)
        Square.save_to_file([square])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 39)

    def test_saving_None_to_file(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_saving_empty_list_to_file(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_without_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_with_extra_arguments(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)

if __name__ == "__main__":
    unittest.main()

