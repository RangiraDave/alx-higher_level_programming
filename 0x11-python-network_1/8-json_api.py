#!/usr/bin/python3
"""
Python script that send a POST request to a URL with a letter as
a parameter and checks if body is properly JSON formatted.
"""

from sys import argv
import requests


q = argv[1] if len(argv) > 1 else ''

r = requests.post('http://0.0.0.0:5000/search_user', json={'q': q})

if not r.json():
    print("No result" if q else "Not a valid JSON")
else:
    id_name = r.json().get('id'), r.json().get('name')
    if None in id_name:
        print("Not a valid JSON")
    else:
        print("[{}] {}".format(*id_name))


if __name__ == "__main__":
    pass
