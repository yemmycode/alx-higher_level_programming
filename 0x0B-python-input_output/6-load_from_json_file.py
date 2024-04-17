#!/usr/bin/python3
"""Module for deserializing an object from a JSON-formatted file."""

import json

def read_json_as_object(json_file):
    """Generates an object from a JSON file.
    Parameters:
        - json_file: The filename of the JSON document
    Returns: The deserialized object
    """

    with open(json_file, 'r', encoding='utf-8') as file:
        return json.load(file)
