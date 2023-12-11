#!/usr/bin/python3
"""This is the base class."""
import json


class Base():
    """Definition of class Base."""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


    @classmethod
    def reset_nb_objects(cls):
        """Reset the __nb_objects attribute."""
        cls.__nb_objects = 0

    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries is []:
            return []
        return json.dumps(list_dictionaries)
