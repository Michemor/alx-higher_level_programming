#!/usr/bin/python3
"""  sends a POST request to the passed URL with the email as a parameter,"""

from urllib.request import urlopen, Request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    val = {"email": argv[2]}
    email = urlencode(val).encode("ascii")

    req = Request(url, email)
    with urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
