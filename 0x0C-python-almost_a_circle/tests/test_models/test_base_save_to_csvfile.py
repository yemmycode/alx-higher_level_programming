#!/usr/bin/python3

"""Unit tests for the base.py module."""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseSaveToFileCSV(unittest.TestCase):
    """Tests for the 'save_to_file_csv' method in the Base class."""

    @classmethod
    def tearDownClass(cls):
        """Clean up files after tests."""
        try:
            os.remove("Rectangle.csv")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.csv")
        except FileNotFoundError:
            pass
        try:
            os.remove("Base.csv")
        except FileNotFoundError:
            pass

    def test_saving_single_rectangle_to_csv(self):
        rectangle = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([rectangle])
        with open("Rectangle.csv", "r") as file:
            self.assertTrue("5,10,7,2,8" in file.read())

    def test_saving_multiple_rectangles_to_csv(self):
        rect1 = Rectangle(10, 7, 2, 8, 5)
        rect2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([rect1, rect2])
        with open("Rectangle.csv", "r") as file:
            self.assertTrue("5,10,7,2,8\n3,2,4,1,2" in file.read())

    def test_saving_single_square_to_csv(self):
        square = Square(10, 7, 2, 8)
        Square.save_to_file_csv([square])
        with open("Square.csv", "r") as file:
            self.assertTrue("8,10,7,2" in file.read())

    def test_saving_multiple_squares_to_csv(self):
        square1 = Square(10, 7, 2, 8)
        square2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([square1, square2])
        with open("Square.csv", "r") as file:
            self.assertTrue("8,10,7,2\n3,8,1,2" in file.read())

    def test_filename_from_class_name_in_save_to_csv(self):
        square = Square(10, 7, 2, 8)
        Base.save_to_file_csv([square])
        with open("Base.csv", "r") as file:
            self.assertTrue("8,10,7,2" in file.read())

    def test_overwriting_file_in_save_to_csv(self):
        square = Square(9, 2, 39, 2)
        Square.save_to_file_csv([square])
        square = Square(10, 7, 2, 8)
        Square.save_to_file_csv([square])
        with open("Square.csv", "r") as file:
            self.assertTrue("8,10,7,2" in file.read())

    def test_saving_empty_list_to_csv(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_csv_without_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_csv_with_extra_arguments(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)

if __name__ == "__main__":
    unittest.main()

