#!/usr/bin/python3
"""
Module providing utility to compare object types.
"""

def is_same_class(obj, a_class):
    """Determine if an object is of a specific type."""
    return isinstance(obj, a_class) == True
