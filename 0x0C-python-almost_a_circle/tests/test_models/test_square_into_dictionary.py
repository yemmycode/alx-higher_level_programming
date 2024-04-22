#!/usr/bin/python3

"""Unit tests for the square model."""

import unittest
from models.base import Base
from models.square import Square

class TestSquareDictionaryConversion(unittest.TestCase):
    """Tests for the Square class's to_dictionary method."""

    def test_output_of_to_dictionary(self):
        square_obj = Square(10, 2, 1, 1)
        expected_output = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(expected_output, square_obj.to_dictionary())

    def test_objects_remain_unchanged(self):
        first_square = Square(10, 2, 1, 2)
        second_square = Square(1, 2, 10)
        second_square.update(**first_square.to_dictionary())
        self.assertNotEqual(first_square, second_square)

    def test_to_dictionary_with_argument(self):
        square_instance = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            square_instance.to_dictionary(1)

if __name__ == '__main__':
    unittest.main()

