#!/usr/bin/pytho
def square_matrix_simple(matrix=[]):
    """
    squares the elements of a matrix
    Input: matrix
    Output: squared matrix
    """
    square_matrix = []
    for row in matrix:
        square_matrix.append(list(map(lambda x: x ** 2, row)))

    return square_matrix
