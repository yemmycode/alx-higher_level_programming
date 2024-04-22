#!/usr/bin/python3

"""Unit tests for the Square model's update method using keyword arguments."""

import unittest
from models.base import Base
from models.square import Square

class TestSquareUpdateKwargs(unittest.TestCase):
    """Tests for the update method of the Square class using keyword arguments."""

    def test_single_kwarg_update(self):
        square = Square(10, 10, 10, 10)
        square.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(square))

    def test_double_kwargs_update(self):
        square = Square(10, 10, 10, 10)
        square.update(size=1, id=2)
        self.assertEqual("[Square] (2) 10/10 - 1", str(square))

    def test_triple_kwargs_update(self):
        square = Square(10, 10, 10, 10)
        square.update(y=1, size=3, id=89)
        self.assertEqual("[Square] (89) 10/1 - 3", str(square))

    def test_full_kwargs_update(self):
        square = Square(10, 10, 10, 10)
        square.update(id=89, x=1, y=3, size=4)
        self.assertEqual("[Square] (89) 1/3 - 4", str(square))

    def test_update_with_width_via_size(self):
        square = Square(10, 10, 10, 10)
        square.update(id=89, size=8)
        self.assertEqual(8, square.width)

    def test_update_with_height_via_size(self):
        square = Square(10, 10, 10, 10)
        square.update(id=89, size=9)
        self.assertEqual(9, square.height)

    def test_update_with_None_id(self):
        square = Square(10, 10, 10, 10)
        square.update(id=None)
        expected_str = "[Square] ({}) 10/10 - 10".format(square.id)
        self.assertEqual(expected_str, str(square))

    def test_update_with_None_id_and_additional_kwargs(self):
        square = Square(10, 10, 10, 10)
        square.update(id=None, size=7, x=18)
        expected_str = "[Square] ({}) 18/10 - 7".format(square.id)
        self.assertEqual(expected_str, str(square))

    def test_update_called_twice(self):
        square = Square(10, 10, 10, 10)
        square.update(id=89, x=1)
        square.update(y=3, x=15, size=2)
        self.assertEqual("[Square] (89) 15/3 - 2", str(square))

    def test_update_with_invalid_size_type(self):
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(size="invalid")

    def test_update_with_size_zero(self):
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.update(size=0)

    def test_update_with_negative_size(self):
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.update(size=-3)

    def test_update_with_invalid_x_type(self):
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            square.update(x="invalid")

    def test_update_with_negative_x(self):
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            square.update(x=-5)

    def test_update_with_invalid_y_type(self):
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            square.update(y="invalid")

    def test_update_with_negative_y(self):
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            square.update(y=-5)

    def test_update_with_args_and_kwargs(self):
        square = Square(10, 10, 10, 10)
        square.update(89, 2, y=6)
        self.assertEqual("[Square] (89) 10/10 - 2", str(square))

    def test_update_with_unrecognized_keys(self):
        square = Square(10, 10, 10, 10)
        square.update(a=5, b=10)
        self.assertEqual("[Square] (10) 10/10 - 10", str(square))

    def test_update_with_mixed_correct_and_wrong_keys(self):
        square = Square(10, 10, 10, 10)
        square.update(size=5, id=89, a=1, b=54)
        self.assertEqual("[Square] (89) 10/10 - 5", str(square))

if __name__ == "__main__":
    unittest.main()

