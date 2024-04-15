#!/usr/bin/python3
"""
This module contains the lookup function which returns a list of available attributes and methods of an object.
"""

def lookup(obj):
    """Returns a list containing the available attributes and methods of an object."""
    return dir(obj)
