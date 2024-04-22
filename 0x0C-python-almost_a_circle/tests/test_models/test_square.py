#!/usr/bin/python3

"""Defines unittests for models/square.py.
Unittest classes:
    TestSquare_instantiation - line 24
    TestSquare_size - line 88
    TestSquare_x - line 166
    TestSquare_y - line 238
    TestSquare_order_of_initialization - line 306
    TestSquare_area - line 322
    TestSquare_stdout - line 343
    TestSquare_update_args - line 426
    TestSquare_update_kwargs - line 538
    TestSquare_to_dictionary - 640
"""
import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquareInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Square class."""

    def test_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_is_rectangle(self):
        self.assertIsInstance(Square(10), Square)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(10, 2, 2)
        s2 = Square(2, 2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def test_size_getter(self):
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def test_size_setter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.size)

    def test_width_getter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.width)

    def test_height_getter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.height)

    def test_x_getter(self):
        self.assertEqual(0, Square(10).x)

    def test_y_getter(self):
        self.assertEqual(0, Square(10).y)


class TestSquareSize(unittest.TestCase):
    """Unittests for testing size initialization of the Square class."""

    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_str_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid")

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5)

    def test_complex_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(5))

    def test_dict_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 1, "b": 2}, 2)

    def test_bool_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True, 2, 3)

    def test_list_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3])

    def test_set_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3}, 2)

    def test_tuple_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3), 2, 3)

    def test_frozenset_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({1, 2, 3, 1}))

    def test_range_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(5))

    def test_bytes_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'Python')

    def test_bytearray_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(b'abcdefg'))

    def test_memoryview_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(b'abcdefg'))

    def test_inf_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))

    def test_nan_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))

    # Test size values
    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)


class TestSquareX(unittest.TestCase):
    """Unittests for testing initialization of Square x attribute."""

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid")

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 5.5)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, complex(5))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {"a": 1, "b": 2}, 2)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, True)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [1, 2, 3])

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {1, 2, 3})

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, (1, 2, 3))

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, frozenset({1, 2, 3, 1}))

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, range(5))

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, b'Python')

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, bytearray(b'abcdefg'))

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, memoryview(b'abcdefg'))

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('inf'))

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('nan'))


class TestSquareY(unittest.TestCase):
    """Unittests for testing initialization of Square y attribute."""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, "invalid")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, 5.5)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, complex(5))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {"a": 1, "b": 2})

    def test_bool_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, True)

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, [1, 2, 3])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {1, 2, 3})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, (1, 2, 3))

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, frozenset({1, 2, 3, 1}))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, range(5))

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, b'Python')

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, bytearray(b'abcdefg'))

    def test_memoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, memoryview(b'abcdefg'))

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, float('inf'))

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, float('nan'))


class TestSquareOrderOfInitialization(unittest.TestCase):
    """Unittests for testing order of initialization of Square class."""

    def test_size_before_xy(self):
        s = Square(1, 2, 3)
        self.assertEqual(1, s.size)
        self.assertEqual(2, s.x)
        self.assertEqual(3, s.y)

    def test_size_before_xy_kwargs(self):
        s = Square(1, y=3, x=2)
        self.assertEqual(1, s.size)
        self.assertEqual(2, s.x)
        self.assertEqual(3, s.y)


class TestSquareArea(unittest.TestCase):
    """Unittests for testing area method of Square class."""

    def test_area(self):
        s = Square(3)
        self.assertEqual(9, s.area())


class TestSquareStdout(unittest.TestCase):
    """Unittests for testing __str__ method of Square class."""

    def test_display_no_xy(self):
        s = Square(3)
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        s.display()
        self.assertEqual("###\n###\n###\n", sys.stdout.getvalue())
        sys.stdout = old_stdout

    def test_display_xy(self):
        s = Square(3, 2, 2)
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        s.display()
        self.assertEqual("\n\n  ###\n  ###\n  ###\n", sys.stdout.getvalue())
        sys.stdout = old_stdout

    def test_str(self):
        s = Square(3, 2, 2, 12)
        self.assertEqual("[Square] (12) 2/2 - 3", str(s))


class TestSquareUpdateArgs(unittest.TestCase):
    """Unittests for testing update method of Square class with *args."""

    def test_update(self):
        s = Square(5, 5, 5, 1)
        s.update(10)
        self.assertEqual(10, s.id)
        self.assertEqual(5, s.size)
        self.assertEqual(5, s.x)
        self.assertEqual(5, s.y)

    def test_update_x(self):
        s = Square(5, 5, 5, 1)
        s.update(10, 2)
        self.assertEqual(10, s.id)
        self.assertEqual(2, s.size)
        self.assertEqual(5, s.x)
        self.assertEqual(5, s.y)

    def test_update_y(self):
        s = Square(5, 5, 5, 1)
        s.update(10, 2, 3)
        self.assertEqual(10, s.id)
        self.assertEqual(2, s.size)
        self.assertEqual(3, s.x)
        self.assertEqual(5, s.y)

    def test_update_size(self):
        s = Square(5, 5, 5, 1)
        s.update(10, 2, 3, 4)
        self.assertEqual(10, s.id)
        self.assertEqual(2, s.size)
        self.assertEqual(3, s.x)
        self.assertEqual(4, s.y)


class TestSquareUpdateKwargs(unittest.TestCase):
    """Unittests for testing update method of Square class with **kwargs."""

    def test_update_x(self):
        s = Square(5, 5, 5, 1)
        s.update(x=7)
        self.assertEqual(7, s.x)

    def test_update_y(self):
        s = Square(5, 5, 5, 1)
        s.update(y=8)
        self.assertEqual(8, s.y)

    def test_update_size(self):
        s = Square(5, 5, 5, 1)
        s.update(size=10)
        self.assertEqual(10, s.size)

    def test_update_id(self):
        s = Square(5, 5, 5, 1)
        s.update(id=15)
        self.assertEqual(15, s.id)

    def test_update_extra(self):
        s = Square(5, 5, 5, 1)
        s.update(bla=1)
        self.assertEqual(5, s.size)
        self.assertEqual(5, s.x)
        self.assertEqual(5, s.y)
        self.assertEqual(1, s.id)


class TestSquareUpdateMixedArgsKwargs(unittest.TestCase):
    """Unittests for testing update method of Square class with *args and **kwargs."""

    def test_update_args_kwargs(self):
        s = Square(5, 5, 5, 1)
        s.update(10, x=7)
        self.assertEqual(10, s.id)
        self.assertEqual(5, s.size)
        self.assertEqual(7, s.x)
        self.assertEqual(5, s.y)

    def test_update_kwargs_args(self):
        s = Square(5, 5, 5, 1)
        s.update(x=8, 20)
        self.assertEqual(20, s.id)
        self.assertEqual(5, s.size)
        self.assertEqual(8, s.x)
        self.assertEqual(5, s.y)

    def test_update_args_args(self):
        s = Square(5, 5, 5, 1)
        s.update(30, 40)
        self.assertEqual(30, s.id)
        self.assertEqual(5, s.size)
        self.assertEqual(5, s.x)
        self.assertEqual(5, s.y)

    def test_update_kwargs_kwargs(self):
        s = Square(5, 5, 5, 1)
        s.update(x=10, y=15)
        self.assertEqual(10, s.x)
        self.assertEqual(15, s.y)

    def test_update_args_kwargs_args_kwargs(self):
        s = Square(5, 5, 5, 1)
        s.update(100, x=15, y=20, size=25)
        self.assertEqual(100, s.id)
        self.assertEqual(25, s.size)
        self.assertEqual(15, s.x)
        self.assertEqual(20, s.y)

