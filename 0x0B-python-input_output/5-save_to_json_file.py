#!/usr/bin/python3
"""Module to serialize an object to a file in JSON format."""

import json

def write_object_as_json(object_to_serialize, target_file):
    """Serializes an object to a file using JSON format.
    Arguments:
        - object_to_serialize: The object to be serialized
        - target_file: The file where the JSON will be saved
    """

    with open(target_file, mode='w', encoding='utf-8') as file:
        json.dump(object_to_serialize, file)
