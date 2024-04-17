#!/usr/bin/python3
"""Module for the Student class.
Establishes the structure of a Student entity.
"""

class Student:
    """A class that represents a student.
    Attributes:
        - first_name
        - last_name
        - age
    Method to_json().
    """

    def __init__(self, first_name, last_name, age):
        """Constructs a Student object."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets a dictionary representation
        of a Student object.
        Parameters:
            - attrs: list of strings representing attributes
        Returns: a dictionary of the object's attributes.
        """

        attribute_dict = {}
        if isinstance(attrs, list) and all(isinstance(item, str) for item in attrs):
            for attribute in attrs:
                if hasattr(self, attribute):
                    attribute_dict[attribute] = getattr(self, attribute)
            return attribute_dict
        return vars(self).copy()
