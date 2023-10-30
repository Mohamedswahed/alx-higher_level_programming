#!/usr/bin/python3.5
"""

multiplies 2 matrices using numpy module

"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ multiplies 2 matrices

    Args:
        m_a: matrix a
        m_b: matrix b

    Returns:
        return the multiplication of two matrices


    """

    return (np.matmul(m_a, m_b))
