#!/usr/bin/python3
"""locked class."""


class LockedClass:
    """
    Prevent the user from dynamically creating new LockedClass
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
