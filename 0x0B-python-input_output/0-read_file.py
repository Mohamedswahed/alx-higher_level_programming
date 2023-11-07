#!/usr/bin/python3
"""Defining read_file function."""


def read_file(filename=""):
    """Reads filename"""
    with open(filename, encoding="utf-8") as fl:
        print(fl.read(), end="")
