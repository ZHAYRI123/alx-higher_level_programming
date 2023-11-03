#!/usr/bin/python3
def matrix_divided(matrix, div):
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(div, (int, float)):
            raise TypeError('div must be a number')
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    for row in matrix:
        for elem in row:
            if not isinstance(elem, (float, int)):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if not all(len(row) == len(matrix[0])for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    my_matrix = list(map(lambda row: list(map(lambda elem: round(float(elem) / div, 2), row)), matrix))
    return (my_matrix)
