#!/usr/bin/python
def square_matrix_simple(matrix=[]):
    if len(matrix) == 0:
        return []
    new_matrix = []
    i = 0
    for row in matrix:
        new_matrix.append([])
        for element in row:
            new_matrix[i].append(element**2)
        i += 1
    return new_matrix
