#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    transpose = []
    for num in range(4):
        square_num = num**2
        transpose.append([row[i] for row in matrix])

