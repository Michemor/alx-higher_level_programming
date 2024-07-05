#!/usr/bin/python3
""" fetches a URL using requests """

import requests

if __name__ == "__main__":
    rep = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(rep.text)))
    print("\t- content: {}".format(rep.text))
