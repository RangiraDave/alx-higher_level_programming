#!/usr/bin/python3
"""
Script to send a request to the url passed as argv and prints its
response body and all handles HTTPError.
"""

from sys import argv
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError


def error_code(url):
    """
    Function to handle program's logic
    """

    req = Request(url)
    try:
        with urlopen(req) as resp:
            print(resp.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code:", e.code)
    except URLError as e:
        print("Error code:", e.code)


if __name__ == "__main__":
    error_code(argv[1])
