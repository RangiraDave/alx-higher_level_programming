#!/usr/bin/python3
"""
Python script that takes in URL, sends a request to it
and displays the body content else error code if the
sstatus code is greater or equal to 400.
"""

from sys import argv
import requests


def error_code(url):
    """
    Function to take care of the logic
    """

    r = requests.get(url)
    if r.status >= 400:
        print("Error code:", r.status)
    else:
        print(r.text)


if __name__ == "__main__":
    error_code(argv[1])
