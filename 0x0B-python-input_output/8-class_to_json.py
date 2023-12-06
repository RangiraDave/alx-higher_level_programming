#!/usr/bin/python3
"""Function to return json-like dictionary for class."""


def class_to_json(obj):
    """Function to return dictionary dedscriptions of class attrb"""

    serialized = {}

    for attrib_name in dir(obj):
        if not attrib_name.startswith('__'):
            attrib_value = getattr(obj, attrib_name)
            if isinstance(attrib_value, (list, int, dict, bool, str)):
                serialized[attrib_name] = attrib_value

    return serialized
