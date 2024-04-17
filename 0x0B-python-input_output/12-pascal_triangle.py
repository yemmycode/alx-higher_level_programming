#!/usr/bin/python3

"""
Function to generate Pascal's triangle
"""

def pascal_triangle(n):
    """
    Generates Pascal's triangle up to a specified number of rows
    """
    p_triangle = []
    for count in range(n):
        row = [1] * (count + 1)
        p_triangle.append(row)
        if count > 1:
            for i in range(1, count):
                row[i] = p_triangle[count - 1][i - 1] + p_triangle[count - 1][i]
    return p_triangle
