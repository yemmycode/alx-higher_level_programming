#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    """
    Executes a function safely.

    Args:
        fct (function): A pointer to the function to be executed.
        *args: Variable-length argument list to pass to the function.

    Returns:
        Any: The result of the function if executed successfully, otherwise None.
    """
    try:
        result = fct(*args) 
        return result
    except Exception as err:
        sys.stderr.write(f"Exception: {err}\n")
        return None
