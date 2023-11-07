#!/usr/bin/python3
""" Defining a function that appends to a text file
"""


def append_write(filename="", text=""):
    """ Function to appends to a text file"""

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
