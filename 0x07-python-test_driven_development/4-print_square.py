#!/usr/bin/python3
"""print_square method module."""


def print_square(size):
    """print a square with # characters method

    Args:
        size: int size of the square's.

    Raises:
        TypeError: If size is not an int.
        ValueError: If size is < 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print((("#" * size + "\n") * size), end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
