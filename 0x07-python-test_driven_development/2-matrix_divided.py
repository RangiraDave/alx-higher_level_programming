#!/usr/bin/python3

def matrix_divided(matrix, div):
    new_mat = []
    i = 0

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for i in range(len(matrix) - 1):
        if len(matrix[i]) != len(matrix[i + 1]):
            raise TypeError("Each row of the matrix must have the same size")

    for el in matrix:
        if type(el) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        for j in el:
            if type(j) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    new_mat = list(map(lambda r: list(map(lambda x: round(x / div, 2) if x != 0 else 0.00, r)), matrix))
    return new_mat
