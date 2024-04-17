#!/usr/bin/python3
"""Module for converting an object to a JSON string.
Provides a function to serialize an object to a JSON-formatted string.
"""

import json

def to_json_string(my_obj):
    """Serializes my_obj to a JSON-formatted str.
    Parameters:
        my_obj (any): The object to serialize.
    Returns:
        str: The JSON string representation of my_obj.
    """
    return json.dumps(my_obj)
