#!/usr/bin/python3
"""
Script to send arequest to URL given as an argument
and print the value of X-Request-Id from the headers' response
"""

import sys
import requests


r = requests.get(sys.argv[1])
print(r.headers["X-Request-Id"])
