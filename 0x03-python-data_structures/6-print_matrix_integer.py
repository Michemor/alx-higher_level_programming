#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """prints integers contained in matrix"""
    for c in range(len(matrix)):
        r = " ".join("{}".format(matrix[c][r]) for r in range(len(matrix[c])))
        print("{}".format(r))
