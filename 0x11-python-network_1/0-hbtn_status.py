#!/usr/bin/python3
"""
Script to fetch https://alx-intranet.hbtn.io/status
"""

import urllib.request


# req = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
    page = resp.read()
    print("Body response:")
    print("\t- type:", type(page))
    print("\t- content:", page)
    print("\t- utf8 content:", page.decode('utf-8'))
