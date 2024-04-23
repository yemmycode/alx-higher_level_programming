#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import pep8

class TestBaseClass(unittest.TestCase):
    """
    Test suite for the Base class in the models module.
    Contains setup, teardown, and a variety of unit tests.
    """

    @classmethod
    def setUpClass(cls):
        """
        Reset the number of objects to zero before each test suite.
        """
        Base._Base__nb_objects = 0

    @classmethod
    def tearDownClass(cls):
        """
        Clean up after the test suite runs.
        """
        pass

    def test_private_attribute(self):
        """
        Test if __nb_objects is a private attribute of Base class.
        """
        self.assertTrue(hasattr(Base, '_Base__nb_objects'))

    def test_pep8_conformance(self):
        """
        Test that the module conforms to PEP8.
        """
        pep8_style = pep8.StyleGuide(quit=True)
        result = pep8_style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Test for the presence of a docstring in the Base module.
        """
        self.assertIsNotNone(Base.__doc__)

    def test_id_auto_assignment(self):
        """
        Test that id is automatically assigned correctly.
        """
        base = Base()
        self.assertEqual(base.id, 1)

    def test_id_manual_assignment(self):
        """
        Test that id can be manually set.
        """
        base = Base(12)
        self.assertEqual(base.id, 12)

    def test_id_sequential_assignment(self):
        """
        Test that ids are assigned sequentially after manual setting.
        """
        Base(12)  # Setting id manually
        base = Base()
        self.assertEqual(base.id, 1)

    def test_id_none_assignment(self):
        """
        Test that passing None assigns the next available id.
        """
        base = Base(None)
        self.assertEqual(base.id, 1)

    def test_id_string_assignment(self):
        """
        Test that id can be set as a string.
        """
        base = Base("Hello")
        self.assertEqual(base.id, "Hello")

    def test_id_float_assignment(self):
        """
        Test that id can be set as a float.
        """
        base = Base(float('inf'))
        self.assertEqual(base.id, float('inf'))

    def test_to_json_string_conversion(self):
        """
        Test converting dictionary to JSON string.
        """
        rectangle = Rectangle(4, 8, 15, 16)
        dictionary = rectangle.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        self.assertIsInstance(json_string, str)

    def test_to_json_string_empty(self):
        """
        Test JSON string representation of an empty list.
        """
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, '[]')

    def test_save_rectangle_to_file(self):
        """
        Test saving a list of Rectangles to a file.
        """
        Rectangle.save_to_file([])
        with open('Rectangle.json', 'r') as file:
            self.assertEqual(file.read(), '[]')

    def test_save_square_to_file(self):
        """
        Test saving a list of Squares to a file.
        """
        Square.save_to_file([])
        with open('Square.json', 'r') as file:
            self.assertEqual(file.read(), '[]')

    def test_json_string_to_dictionary_conversion(self):
        """
        Test converting JSON string to dictionary.
        """
        dictionary_list = [{'id': 1, 'x': 2, 'size': 10, 'y': 1},
                           {'id': 89, 'x': 0, 'size': 4, 'y': 3}]
        json_string = Base.to_json_string(dictionary_list)
        self.assertEqual(json.loads(json_string), dictionary_list)

    def test_from_json_string_to_list_conversion(self):
        """
        Test converting JSON string to list of dictionaries.
        """
        json_string = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        result = Base.from_json_string(json_string)
        self.assertIsInstance(result, list)

    def test_from_json_string_empty(self):
        """
        Test converting an empty JSON string to an empty list.
        """
        self.assertEqual(Base.from_json_string(None), [])

if __name__ == '__main__':
    unittest.main()
        
