#!/usr/bin/python3
"""
Python script to take in repo name and author name
use github api to print 10 commits from newest to oldest.
"""

import sys
import requests


if __name__ == "__main__":

    Repo = sys.argv[1]
    Owner = sys.argv[2]

    url = f"http://api.github.com/repos/{Owner}/{Repo}/commits"

    r = requests.get(url)

    commits = r.json()
    for commit in commits[:10]:
        sha = commit['sha']
        author = commit['commit']['author']['name']
        print("{}: {}".format(sha, author))
