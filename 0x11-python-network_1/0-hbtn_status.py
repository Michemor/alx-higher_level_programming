#!/usr/bin/python3
""" fetches a URL using urllib """

from urllib.request import urlopen

url = 'https://alx-intranet.hbtn.io/status'
with urlopen(url) as response:
    body = response.read()
    print("Body response: ")
    print("\t - type: {}".format(type(body)))
    print("\t - content: {}".format(body))
    print("\t - utf8 content: {}".format(body.decode('utf-8')))
