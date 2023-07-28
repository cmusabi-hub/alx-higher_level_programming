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
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    
    if not isinstance(m_a[0], list):
        raise TypeError("m_a must be a list of list")
    if not isinstance(m_b[0], list):
        raise TypeError("m_b must be a list of list")

    if m_a == []:
        raise ValueError("m_a can't be empty")
    if m_b == []:
        raise ValueError("m_b can't be emty")

    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be the same size")
    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    product = []
    
    for row in range(len(m_a)):
        row_list = []
        for column in range(len(m_b[0])):
            product_element = 0
            for column_row in range(len(m_a[0])):
                product_element += m_a[row][column_row] * m_b[column_row][column]
            row.append(product_element)
        product.append(row)

    return (product)
