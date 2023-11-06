#!/usr/bin/python3
"""
module for MyList class
"""


class MyList(list):
    """subclass of list"""
    def __init__(self):
        """initializes bject"""
        super().__init__()

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
