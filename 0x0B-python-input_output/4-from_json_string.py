#!/usr/bin/python3
"""
Function to deserialize a JSON string into a Python object.
"""

import json

def from_json_string(my_str):
    """
    Converts a JSON string into a corresponding Python object.
    Args:
        my_str (str): A JSON string to be deserialized.
    Returns:
        The Python object represented by the JSON string.
    """
    return json.loads(my_str)
