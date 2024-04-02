#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """
    Prints an integer followed by a new line.

    Args:
        value: Any type (integer, string, etc.).

    Returns:
        bool: True if value is an integer and printed successfully, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as err:
        sys.stderr.write(f"Exception: {err}\n")
        return False
