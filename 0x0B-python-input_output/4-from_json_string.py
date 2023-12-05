#!/usr/bin/python3
"""Lets return it to object data"""
import json


def from_json_string(my_str):
    """This function converts json strings to data objects."""

    return json.load("my_str")
