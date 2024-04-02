#!/usr/bin/python3
def raise_exception_msg(message=""):
    """
    Raises a custom exception with the given message.

    Args:
        message (str): The custom error message to be included in the exception.

    Raises:
        NameError: Always raises a NameError with the provided message.
    """
    raise NameError(message)
