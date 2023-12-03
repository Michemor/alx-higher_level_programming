#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """prints integers contained in matrix"""
    for c in range(len(matrix)):
        for r in range(len(matrix[0])):
            print("{}".format(matrix[c][r]), end=" ")
        print("".format())
