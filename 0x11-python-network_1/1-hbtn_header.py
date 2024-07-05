#!/usr/bin/python3
""" displays the value of a key in the header """

from urllib.request import urlopen
from sys import argv

if __name__ == "__main__":
    with urlopen(argv[1]) as response:
        print(response.getheader('X-Request-Id'))
