#!/usr/bin/python3
"""
Module for checking object class relationships.
"""

def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of, or inherits from, a_class."""
    return isinstance(obj, a_class)
