#!/usr/bin/python3

"""Script to append command-line arguments to a list and store it in a JSON file."""
import sys

if __name__ == "__main__":
    serialize_to_json = __import__('5-save_to_json_file').save_to_json_file
    deserialize_from_json = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        arguments_list = deserialize_from_json("add_item.json")
    except FileNotFoundError:
        arguments_list = []
    arguments_list.extend(sys.argv[1:])
    serialize_to_json(arguments_list, "add_item.json")
