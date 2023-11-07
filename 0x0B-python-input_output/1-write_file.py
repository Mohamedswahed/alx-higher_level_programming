#!/usr/bin/python3
""" defining function that writes to a text file"""


def write_file(filename="", text=""):
    """ Function that write filename with utf-8"""

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
