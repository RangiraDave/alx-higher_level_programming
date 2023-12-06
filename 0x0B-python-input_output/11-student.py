#!/usr/bin/python3
"""Lets add a functionality to load json from a file."""


class Student():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Function to return json-like dictionary."""

        if attrs is None:
            dictionary = {
                    'first_name': self.first_name,
                    'last_name': self.last_name,
                    'age': self.age
                    }
            return dictionary

        dictionary = {}
        for at in attrs:
            if hasattr(self, at):
                at_value = getattr(self, at)
                dictionary[at] = at_value

        return dictionary

    def reload_from_json(self, json):
        """Function to repalce all class attributes."""

        self.first_name = json['first_name']
        self.last_name = json['last_name']
        self.age = json['age']
