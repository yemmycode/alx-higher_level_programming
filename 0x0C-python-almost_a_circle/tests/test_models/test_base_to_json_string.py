#!/usr/bin/python3

"""Unit tests for the base.py module."""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseToJsonString(unittest.TestCase):
    """Tests for the 'to_json_string' method of the Base class."""

    def test_json_string_type_for_rectangle(self):
        rectangle = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(type(Base.to_json_string([rectangle.to_dictionary()])), str)

    def test_json_string_length_with_one_rectangle(self):
        rectangle = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(len(Base.to_json_string([rectangle.to_dictionary()])), 53)

    def test_json_string_length_with_two_rectangles(self):
        rect1 = Rectangle(2, 3, 5, 19, 2)
        rect2 = Rectangle(4, 2, 4, 1, 12)
        dictionaries = [rect1.to_dictionary(), rect2.to_dictionary()]
        self.assertEqual(len(Base.to_json_string(dictionaries)), 106)

    def test_json_string_type_for_square(self):
        square = Square(10, 2, 3, 4)
        self.assertEqual(type(Base.to_json_string([square.to_dictionary()])), str)

    def test_json_string_length_with_one_square(self):
        square = Square(10, 2, 3, 4)
        self.assertEqual(len(Base.to_json_string([square.to_dictionary()])), 39)

    def test_json_string_length_with_two_squares(self):
        square1 = Square(10, 2, 3, 4)
        square2 = Square(4, 5, 21, 2)
        dictionaries = [square1.to_dictionary(), square2.to_dictionary()]
        self.assertEqual(len(Base.to_json_string(dictionaries)), 78)

    def test_json_string_with_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_json_string_with_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_without_arguments(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_with_extra_arguments(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

