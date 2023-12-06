#!/usr/bin/python3
"""Class Student that deals with student's data."""


class Student():
    """The Student class is defined here."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Function to return student's info json-like dictionary"""
        stud_dict = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
                }
#        for attrib_name in dir(Student):
#            if not attrib_name.startswith('__'):
#                attrib_value = getattr(Student, attrib_name)
#                if isinstance(attrib_value, (list, int, dict, bool, str)):
#                    stud_dict[attrib_name] = attrib_value

        return stud_dict
