#!/usr/bin/python3
"""
Script to fetch the url
"""

import requests


r = requests.get('https://alx-intranet.hbtn.io/status')
print("Body response:")
print("\t- type:", type(r.content.decode('utf-8')))
print("\t- content:", r.text)
