#!/usr/bin/python3
"""
Script to send a request to the URL given as an argument
and displays the value of X-Request-Id variable found in its header
"""

from sys import argv
from urllib.request import urlopen


def send_request(url):
    """
    Function to send a request to the url given
    """

    with urlopen(url) as resp:
        content = resp.headers
        print(content["X-Request-Id"])


if __name__ == "__main__":
    send_request(argv[1])
