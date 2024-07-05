#!/usr/bin/python3
"""
sends a POST request to the passed URL
the email is passed as a parameter
"""

from urllib.request import urlopen, Request
from sys import argv
from urllib.parse import urlencode

if __name__ == "__main__":
    url = argv[1]
    data = {"email": argv[2]}
    email = urlencode(data).encode("ascii")
    req = Request(url, email)
    with urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
