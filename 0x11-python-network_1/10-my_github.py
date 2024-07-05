#!/usr/bin/python3
"""
takes your GitHub credentials (username and password)
Uses the GitHub API to display your id
"""

import requests
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]

    url = f"https://api.github.com/users/{username}"
    headers = {"Accept": "application/vnd.github+json",
                "Authorization": f"{password}",
                "X-Github-Api-Version": "2022-11-28"}
    response = requests.get(url, headers=headers)
    print(response.json().get("id"))
