#!/usr/bin/python3
"""
Script to send arequest to URL given as an argument
and print the value of X-Request-Id from the headers' response
"""

from sys import argv
import requests


def fetch(url):
    """
    Function to handle the logic
    """

    r = requests.get(url)
    print(r.headers["X-Request-Id"])


if __name__ == "__main__":
    fetch(argv[1])
