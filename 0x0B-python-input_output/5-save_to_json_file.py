#!/usr/bin/python3
"""Lets save an object to a json file shall we?"""
import json


def save_to_json_file(my_obj, filename):
    """This is the function that does that."""

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
