#!/usr/bin/python3
"""
Script to send a request to the url passed as argv and prints its
response body and all handles HTTPError.
"""

from sys import argv
from urllib.request import Request, urlopen
from urllib.error import HTTPError


def error_code(url):
    """
    Function to handle program's logic
    """

    req = Request(url)
    with urlopen(req) as resp:
        if HTTPError:
            print(HTTPError.status)
        page = resp.read()
        print(page.decode('utf-8'))


if __name__ == "__main__":
    error_code(argv[1])
