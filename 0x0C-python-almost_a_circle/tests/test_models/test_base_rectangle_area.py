#!/usr/bin/python3

"""Unit tests for rectangle model."""

import unittest
from models.rectangle import Rectangle

class RectangleAreaTest(unittest.TestCase):
    """Tests for the area method in the Rectangle class."""

    def test_small_area(self):
        rect = Rectangle(10, 2)
        self.assertEqual(rect.area(), 20)

    def test_large_area(self):
        rect = Rectangle(999999999999999, 999999999999999999)
        self.assertEqual(rect.area(), 999999999999998999000000000000001)

    def test_area_after_attribute_change(self):
        rect = Rectangle(2, 10)
        rect.width, rect.height = 7, 14
        self.assertEqual(rect.area(), 98)

    def test_area_with_extra_argument(self):
        rect = Rectangle(2, 10)
        with self.assertRaises(TypeError):
            rect.area(1)

class RectangleDisplayTest(unittest.TestCase):
    """Tests for the __str__ and display methods in the Rectangle class."""

    @staticmethod
    def stdout_capture(rectangle, method_name):
        """Captures stdout output from a rectangle method."""
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output
        if method_name == "print":
            print(rectangle)
        else:
            rectangle.display()
        sys.stdout = sys.__stdout__
        return captured_output.getvalue()

    # Tests for __str__ method
    def test_print_str(self):
        rect = Rectangle(4, 6)
        output = self.stdout_capture(rect, "print")
        expected_output = "[Rectangle] ({}) 0/0 - 4/6\n".format(rect.id)
        self.assertEqual(expected_output, output)

    def test_str_with_x(self):
        rect = Rectangle(5, 5, 1)
        expected_output = "[Rectangle] ({}) 1/0 - 5/5".format(rect.id)
        self.assertEqual(expected_output, str(rect))

    def test_str_with_x_y(self):
        rect = Rectangle(1, 8, 2, 4)
        expected_output = "[Rectangle] ({}) 2/4 - 1/8".format(rect.id)
        self.assertEqual(expected_output, str(rect))

    def test_str_with_all_attributes(self):
        rect = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(rect))

    def test_str_after_attribute_change(self):
        rect = Rectangle(7, 7, 0, 0, [4])
        rect.width, rect.height, rect.x, rect.y = 15, 1, 8, 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(rect))

    def test_str_with_extra_argument(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            rect.__str__(1)

    # Tests for display method
    def test_display_basic(self):
        rect = Rectangle(2, 3)
        output = self.stdout_capture(rect, "display")
        self.assertEqual("##\n##\n##\n", output)

    def test_display_with_x(self):
        rect = Rectangle(3, 2, 1)
        output = self.stdout_capture(rect, "display")
        self.assertEqual(" ###\n ###\n", output)

    def test_display_with_y(self):
        rect = Rectangle(4, 5, 0, 1)
        output = self.stdout_capture(rect, "display")
        expected_output = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(expected_output, output)

    def test_display_with_x_y(self):
        rect = Rectangle(2, 4, 3, 2)
        output = self.stdout_capture(rect, "display")
        expected_output = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(expected_output, output)

    def test_display_with_extra_argument(self):
        rect = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            rect.display(1)

if __name__ == "__main__":
    unittest.main()

