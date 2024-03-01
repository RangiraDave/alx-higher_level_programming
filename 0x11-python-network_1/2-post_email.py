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

    dta = urllib.parse.urlencode({'email': email})
    dta = dta.encode('ascii')

    with urllib.request.urlopen(url, data=dta) as resp:
        content = resp.read()
        print("Your email is:", content.decode('utf-8'))


if __name__ == "__main__":
    post_email(argv[1], argv[2])
