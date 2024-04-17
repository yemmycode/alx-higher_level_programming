#!/usr/bin/python3
"""Module 11-student.
Defines a Student class with serialization and update capabilities.
"""

class Student:
    """A class that encapsulates the details of a student.
    Attributes available for public access:
        - first_name
        - last_name
        - age
    Includes methods for JSON serialization and instance updating.
    """

    def __init__(self, first_name, last_name, age):
        """Sets up a new Student object."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Provides a dictionary representation of the Student object.
        Parameters:
            - attrs: a list of attribute names to include
        Returns: a dictionary with the object's data.
        """

        attribute_dictionary = {}
        if attrs and all(isinstance(attribute, str) for attribute in attrs):
            for attribute in attrs:
                if hasattr(self, attribute):
                    attribute_dictionary[attribute] = getattr(self, attribute)
            return attribute_dictionary
        return vars(self)

    def reload_from_json(self, json_attributes):
        """Updates the attributes of the Student object.
        Parameters:
            - json_attributes: a dictionary of attributes to update
        """

        for key, value in json_attributes.items():
            setattr(self, key, value)
