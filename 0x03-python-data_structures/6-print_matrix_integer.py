#!/usr/bin/python3
def print_matrix_integer(matrix=[]):
    i = 0
    if matrix:
        for row in matrix:
            for elt in row:
                if i == (len(row) - 1):
                    print("{:d}".format(elt), end="")
                else:
                    print("{:d} ".format(elt), end=" "),
                i += 1
            print('$')
            i = 0
    else:
        print('$')
