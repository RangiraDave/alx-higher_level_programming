#!/usr/bin/python3
"""
Python script that send a POST request to a URL with a letter as
a parameter and checks if body is properly JSON formatted.
"""

from sys import argv
import requests


def json_check(letter):
    """
    Function to handle logic.
    """

    q = letter if letter 1 else ''

    with requests.post('http://0.0.0.0:5000/search_user', data={'q': q}) as resp:
        try:
            page = resp.json()
            if page:
                print("[{}] {}".format(page.get('id'), page.get('name')
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")


if __name__ == "__main__":
    json_check(argv[1])
