#!/usr/bin/python3
"""
Module: open, write, read, closes files
"""


def write_file(filename="", text=""):
    """opens a file for writing to it"""
    nbchars = 0
    with open(filename, 'w', encoding="UTF8") as file:
        nbchars = file.write(text)
    return (nbchars)
