#!/usr/bin/python3
"""
Module defining inheritance checks.
"""

def inherits_from(obj, a_class):
    """Check if obj's type is a derived class of a_class."""
    return issubclass(type(obj), a_class) and not type(obj) is a_class
