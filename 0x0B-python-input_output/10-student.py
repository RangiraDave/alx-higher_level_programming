#!/usr/bin/python3
"""Updated class Student to use attrb in to_json method."""


class Student():
    """Definition of the class."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Function to return dictionary dipending on the attrs given."""
        if attrs is None:
            dictionary = {
                    'first_name': self.first_name,
                    'last_name': self.last_name,
                    'age': self.age
                    }
            return dictionary
        dictionary = {}
        for at in list(attrs):
            if hasattr(self, at):
                at_value = getattr(self, at)
                dictionary[at] = at_value
        return dictionary
