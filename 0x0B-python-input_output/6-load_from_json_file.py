#!/usr/bin/python3
"""Lets now convert json to object."""
import json
from io import StringIO


def load_from_json_file(filename):
    """This function loads contents from json file."""

    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
