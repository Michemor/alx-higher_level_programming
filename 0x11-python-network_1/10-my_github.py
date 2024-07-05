#!/usr/bin/python3
"""
takes your GitHub credentials (username and password)
Uses the GitHub API to display your id
"""

import requests
from sys import argv
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    credentials = HTTPBasicAuth(argv[1], argv[2])
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=credentials)
    print(response.json().get("id"))
