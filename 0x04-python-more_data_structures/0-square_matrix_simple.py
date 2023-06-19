#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    size = len(matrix)
    new_matrix = [None] * size
    for i in range(len(matrix)):
        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))
    return new_matrix
