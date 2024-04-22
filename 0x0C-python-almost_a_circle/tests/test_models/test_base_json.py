#!/usr/bin/python3

"""Unit tests for the base.py module."""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseFromJsonString(unittest.TestCase):
    """Tests for the 'from_json_string' method in the Base class."""

    def test_type_returned_from_json_string(self):
        input_list = [{"id": 89, "width": 10, "height": 4}]
        json_input = Rectangle.to_json_string(input_list)
        output_list = Rectangle.from_json_string(json_input)
        self.assertIsInstance(output_list, list)

    def test_single_rectangle_from_json_string(self):
        input_list = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_input = Rectangle.to_json_string(input_list)
        output_list = Rectangle.from_json_string(json_input)
        self.assertEqual(input_list, output_list)

    def test_multiple_rectangles_from_json_string(self):
        input_list = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3}
        ]
        json_input = Rectangle.to_json_string(input_list)
        output_list = Rectangle.from_json_string(json_input)
        self.assertEqual(input_list, output_list)

    def test_single_square_from_json_string(self):
        input_list = [{"id": 89, "size": 10, "x": 7, "y": 8}]
        json_input = Square.to_json_string(input_list)
        output_list = Square.from_json_string(json_input)
        self.assertEqual(input_list, output_list)

    def test_multiple_squares_from_json_string(self):
        input_list = [
            {"id": 89, "size": 10, "x": 7, "y": 8},
            {"id": 7, "size": 1, "x": 1, "y": 3}
        ]
        json_input = Square.to_json_string(input_list)
        output_list = Square.from_json_string(json_input)
        self.assertEqual(input_list, output_list)

    def test_from_json_string_with_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_with_empty_string(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_without_arguments(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_with_multiple_arguments(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)

if __name__ == "__main__":
    unittest.main()

