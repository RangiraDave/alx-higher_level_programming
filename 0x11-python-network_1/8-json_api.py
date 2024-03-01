#!/usr/bin/python3
"""
Python script that send a POST request to a URL with a letter as
a parameter and checks if body is properly JSON formatted.
"""

import sys
import requests as rqs


if __name__ == "__main__":
    """
    Function to handle logic.
    """

    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 2:
        q = {"q": sys.argv[1]}
    else:
        q = {"q": ""}
    with rqs.post(url, data=q) as resp:
        try:
            page = resp.json()
            if page:
                print("[{}] {}".format(page.get("id"), page.get("name")))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
