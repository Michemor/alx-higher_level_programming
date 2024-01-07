#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    divides each element of a matrix by the number div
    Args:
        matrix : to be divided
        div : number which divides each element of the matrix
    Returns:
        a new matrix divided
    """
    new_matrix = []
    first_row_len = len(matrix[0])
    for sub in matrix:
        for item in sub:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    # check for whether each row of the matrix is the same
    for row in matrix[1:]:
        if len(row) != first_row_len:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for sub in matrix:
        inner = []
        for n in sub:
            result = round(n / div, 2)
            inner.append(result)
        new_matrix.append(inner)
    return (new_matrix)
