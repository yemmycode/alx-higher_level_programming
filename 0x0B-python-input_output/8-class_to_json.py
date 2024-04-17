#!/usr/bin/python3
"""Module for converting a class instance to a dictionary suitable for JSON serialization."""

def class_to_json(obj):
    """Generates a dictionary from an object's attributes.

    Arguments:
        - obj: The instance of a class to serialize.

    Returns: A dictionary of the object's attributes.
    """

    return obj.__dict__
