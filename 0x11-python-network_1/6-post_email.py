#!/usr/bin/python3
"""
Script that takes in url and email address
sends a post request to that url with the email parameter
displays the response body.
"""

from sys import argv
import requests


def post_e(url, email):
    """
    Function to carryout the logic
    """

    r = requests.post(url, data={'email': str(email)})
    print(r.text)


if __name__ == "__main__":
    post_e(argv[1], argv[2])
