#!/usr/bin/python3
"""
Python script to post email (passed as argv) to the
URL also passed as argument and display response body
"""

from sys import argv
import urllib.parse
import urllib.request


def post_email(url, email):
    """
    Function to handle the logic
    """

    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as resp:
        if resp.status == 200:
            content = resp.read()
            print("Your email is:", content.decode('utf-8'))
        else:
            print("Error: Request failed with status code", content.status)


if __name__ == "__main__":
    post_email(argv[1], argv[2])
