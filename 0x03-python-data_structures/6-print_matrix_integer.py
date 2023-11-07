#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col_num in range(len(row)):
            print("{:d}".format(row[col_num]), end='')
            if col_num < len(row) - 1:
                print("{}".format(" "), end='')
        print("{}".format(''))
