#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Raises:
        ValueError: If matrices can't be multiplied or empty.
        TypeError: If inputs are not lists or not containing only ints/floats.
    Returns:
        np.ndarray: The resulting matrix.
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("Inputs must be lists")

    if len(m_a) == 0 or len(m_a[0]) == 0 or len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("Empty matrices")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("Input matrices must be list of lists")

    if not all(isinstance(ele, (int, float)) for row in m_a for ele in row) or not all(isinstance(ele, (int, float)) for row in m_b for ele in row):
        raise TypeError("Matrices must contain only integers or floats")

    if len(m_a[0]) != len(m_b):
        raise ValueError("Matrices can't be multiplied")

    return np.matmul(m_a, m_b)
