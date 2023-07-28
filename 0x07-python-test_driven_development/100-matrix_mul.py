#!/usr/bin/python3
"""Function that multiplies matrices"""


def matrix_mul(m_a, m_b):
    """
    Args:
     m_a: first matrix.
     m_b: second matrix.

    Returns:
     The product of the two matrices.

    Raises:
     Exceptions if detected

    """

    if not isinstance(m_a, list) or not all(isinstance
                                            (row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not isinstance(m_b, list) or not all(isinstance
                                            (row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")

    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    if not m_a:
        raise ValueError("m_a can't be empty")

    if not m_b:
        raise ValueError("m_b can't be empty")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise ValueError("each row of m_a must be the same size")

    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise ValueError("each row of m_b must be the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    product = []

    for row in range(len(m_a)):
        row_list = []
        for column in range(len(m_b[0])):
            product_element = 0
            for column_row in range(len(m_a[0])):
                product_element += m_a[row][column_row] * \
                    m_b[column_row][column]
            row_list.append(product_element)
        product.append(row_list)

    return (product)
