#!/usr/bin/python3
"""
Module: open, write, read and close file
"""

def append_write(filename="", text=""):
    """
    writes to file and doesnt overwrite; adds text to previously
    existing file
    """
    nbchars = 0
    with open(filename, 'a', encoding="UTF8") as f:
        nbchars = f.write(text)
    return (nbchars)
