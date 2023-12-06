#!/usr/bin/python3
"""pascal_triangle implementer function."""


def pascal_triangle(n):
    """Function to return the Pascal's triangle as list of lists."""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, len(triangle[-1])):
            row.append(triangle[-1][j - 1] + triangle[-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
