#!/usr/bin/python3
"""  sends a POST request to the passed URL with the email as a parameter,"""

from urllib.request import urlopen, Request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = urlencode({'email': argv[2]})
    email = email.encode('utf-8')
    req = Request(url, email)
    with urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))

