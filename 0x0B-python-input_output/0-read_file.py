#!/usr/bin/python3
def read_file(filename=""):
    """
    opens a file passed as argument to the function and read it
    """
    with open(filename, 'r', encoding="UTF8") as f:
        for line in f:
            print(line, end="")
