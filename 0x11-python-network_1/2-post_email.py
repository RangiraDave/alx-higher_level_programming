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

    data = urllib.parse.urlencode({'Email': email})
    data = data.encode('ascii')

    with urllib.request.urlopen(url, data=data) as resp:
        if resp.status == 200:
            content = resp.read()
            print("Your email is:", content.decode('utf-8'))
        else:
            print("Error: Request failed with status code", resp.status)


if __name__ == "__main__":
    post_email(argv[1], argv[2])
