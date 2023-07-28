#!/usr/bin/python3
import numpy as np
"""Module for multiplication of matrices"""


def lazy_matrix_mul(m_a, m_b):
    """
    m_a is first matrix
    m_b is the second matrix
    """
    matri_mult = np.dot(m_a, m_b)

    return (matri_mult)
