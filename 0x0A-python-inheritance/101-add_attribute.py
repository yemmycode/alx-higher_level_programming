#!/usr/bin/python3
""" A module for adding attributes """

def add_attribute(a_class, name, value):
    """ Adds a new attribute to an object if possible """
    if "__dict__" in dir(a_class):
        setattr(a_class, name, value)
    else:
        raise TypeError("can't add new attribute")
