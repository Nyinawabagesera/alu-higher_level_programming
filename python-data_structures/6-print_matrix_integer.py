#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print(" ")
        return
    for row in matrix:
        for i, num in enumerate(row):
            if i < len(row) - 1:
                print("{:d} ".format(num), end="")
            else:
                print("{:d}".format(num))
    if not matrix or all(not row for row in matrix):
            print("")
            return
