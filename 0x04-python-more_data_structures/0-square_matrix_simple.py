#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix = matrix[i][j] ** 2
    return new_matrix
