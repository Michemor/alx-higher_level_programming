#!/usr/bin/python3
"""
sends a POST request to the passed URL
adds the email as a parameter
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    rep = requests.get(url)
    if rep.status_code >= 400:
        print("Error code: {}".format(rep.status_code))
    else:
        print(rep.content.decode("utf-8"))
