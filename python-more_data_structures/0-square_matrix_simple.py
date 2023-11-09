#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    y = transpose(map(square_matrix_simple, matrix))
