#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[None]*len(matrix[0])]*len(matrix)
    i = 0
    j = 0
    for row in matrix:
        for element in row:
            new_matrix[i][j] = element**2
            j += 1
        i += 1
        j = 0
    return new_matrix
