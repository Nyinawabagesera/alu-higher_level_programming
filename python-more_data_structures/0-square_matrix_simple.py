#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        print()
    transpose(map(num*num, matrix))
