#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_m = []
    new_m = list([row[i] ** 2 for i in range(len(row))] for row in matrix)
    return new_m
