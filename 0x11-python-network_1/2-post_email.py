#!/usr/bin/python3
"""
Python script to post email (passed as argv) to the
URL also passed as argument and display response body
"""

from sys import argv
from urllib.parse import urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError


def post_email(url, email):
    """
    Function to handle the logic
    """

    values = {'email': email}
    data = urlencode(values).encode('ascii')

    with urlopen(url, data=data) as resp:
        if resp.status == 200:
            print("Your email is:", resp.read().decode('utf-8'))
        else:
            print("Error: Request failed with status code", resp.status)


if __name__ == "__main__":
    post_email(argv[1], argv[2])
