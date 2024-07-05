#!/usr/bin/python3
"""
sends a POST request to the passed URL
adds the email as a parameter
"""

import requests
from sys import argv

if __name__ == "__main__":
    email = {"email": argv[2]}
    rep = requests.post(argv[1], email)
    print(rep.content.decode("utf-8"))
