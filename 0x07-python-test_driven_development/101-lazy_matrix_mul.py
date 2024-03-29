#!/usr/bin/python3
import numpy as np
"""Module for multiplication of matrices"""


def lazy_matrix_mul(m_a, m_b):
    """
    m_a is first matrix
    m_b is the second matrix
    """
    return (np.matmul(m_a, m_b))
