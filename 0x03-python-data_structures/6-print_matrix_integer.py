#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col_num in range(len(row)):
            print("{:2d}".format(row[col_num]), end = '')
        print()
