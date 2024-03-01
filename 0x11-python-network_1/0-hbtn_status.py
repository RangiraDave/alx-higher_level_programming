#!/usr/bin/python3
"""
Script to fetch https://alx-intranet.hbtn.io/status
"""

import urllib.request


req = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(req) as resp:
    print("Body response:")
    print("\t- type:", type(resp.read()))
    print("\t- content:", resp.read())
    print("\t- utf8 content:", resp.read().decode('utf-8'))
