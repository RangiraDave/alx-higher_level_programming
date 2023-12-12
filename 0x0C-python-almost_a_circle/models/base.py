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

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries is '[]':
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        fileName = str(cls.__name__) + '.json'
        if list_objs is None:
            list_objs = []

        j_list = [i.to_dictionary() for i in list_objs]
        j_string = cls.to_json_string(j_list)
        with open(fileName, 'w+', encoding='utf-8') as f:
            f.write(j_string)

    @staticmethod
    def from_json_string(json_string):
        if not json_string or json_string is None:
            return []
        else:
            return json.dump(json_string)
