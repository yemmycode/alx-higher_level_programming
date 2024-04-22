#!/usr/bin/python3

"""Unit tests for the to_dictionary method in the Rectangle class."""

import unittest
from models.rectangle import Rectangle

class RectangleDictionaryTest(unittest.TestCase):
    """Tests for converting Rectangle instances to dictionaries."""

    def test_output_to_dictionary(self):
        rect = Rectangle(10, 2, 1, 9, 5)
        expected = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(expected, rect.to_dictionary())

    def test_no_change_to_original_object(self):
        rect1 = Rectangle(10, 2, 1, 9, 5)
        rect2 = Rectangle(5, 9, 1, 2, 10)
        rect2.update(**rect1.to_dictionary())
        self.assertNotEqual(rect1, rect2)

    def test_to_dictionary_with_argument(self):
        rect = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            rect.to_dictionary(1)

if __name__ == "__main__":
    unittest.main()

