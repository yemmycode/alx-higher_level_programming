#!/usr/bin/python3

"""Unit tests for the base.py module."""

import unittest
from models.base import Base

class TestBaseInstantiation(unittest.TestCase):
    """Tests for creating instances of the Base class."""

    def test_creation_without_arguments(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id + 1, base2.id)

    def test_creation_of_multiple_bases(self):
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base1.id + 2, base3.id)

    def test_creation_with_None_as_id(self):
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id + 1, base2.id)

    def test_creation_with_specific_id(self):
        self.assertEqual(Base(12).id, 12)

    def test_id_assignment_after_specific_id(self):
        base1 = Base()
        Base(12)
        base3 = Base()
        self.assertEqual(base1.id + 1, base3.id)

    def test_public_id_attribute(self):
        base = Base(12)
        base.id = 15
        self.assertEqual(base.id, 15)

    def test_private_number_of_instances(self):
        with self.assertRaises(AttributeError):
            Base(12).__nb_objects

    def test_creation_with_string_id(self):
        self.assertEqual(Base("hello").id, "hello")

    def test_creation_with_float_id(self):
        self.assertEqual(Base(5.5).id, 5.5)

    def test_creation_with_complex_number_id(self):
        self.assertEqual(Base(complex(5)).id, complex(5))

    def test_creation_with_dictionary_id(self):
        self.assertEqual(Base({"a": 1, "b": 2}).id, {"a": 1, "b": 2})

    def test_creation_with_boolean_id(self):
        self.assertEqual(Base(True).id, True)

    def test_creation_with_list_id(self):
        self.assertEqual(Base([1, 2, 3]).id, [1, 2, 3])

    def test_creation_with_tuple_id(self):
        self.assertEqual(Base((1, 2)).id, (1, 2))

    def test_creation_with_set_id(self):
        self.assertEqual(Base({1, 2, 3}).id, {1, 2, 3})

    def test_creation_with_frozenset_id(self):
        self.assertEqual(Base(frozenset({1, 2, 3})).id, frozenset({1, 2, 3}))

    def test_creation_with_range_id(self):
        self.assertEqual(Base(range(5)).id, range(5))

    def test_creation_with_bytes_id(self):
        self.assertEqual(Base(b'Python').id, b'Python')

    def test_creation_with_bytearray_id(self):
        self.assertEqual(Base(bytearray(b'abcefg')).id, bytearray(b'abcefg'))

    def test_creation_with_memoryview_id(self):
        self.assertEqual(Base(memoryview(b'abcefg')).id, memoryview(b'abcefg'))

    def test_creation_with_infinite_id(self):
        self.assertEqual(Base(float('inf')).id, float('inf'))

    def test_creation_with_NaN_id(self):
        nan_id = Base(float('nan')).id
        self.assertTrue(nan_id != nan_id)  # NaN is not equal to itself

    def test_creation_with_multiple_arguments(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

if __name__ == "__main__":
    unittest.main()

