#!/usr/bin/python3
""" define a function called matrix_divided"""


def matrix_divided(matrix, div):
    """divide a square matrix
    :param matrix: (list of lists)
    :param div: (int, float)

    Return: new matrix
    """
    if type(matrix) is list:
        for i in range(len(matrix)):
            if type(matrix[i]) is not list:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )
            for j in range(len(matrix[i])):
                if type(matrix[i][j]) not in (int, float):
                    raise TypeError(
                        "matrix must be a matrix (list of lists) of integers/floats"
                    )
    shape = matrix_shape(matrix)
    if not shape:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(len(matrix[i])):
            new_matrix[i].append(round(matrix[i][j] / div, 2))
    return new_matrix


def matrix_shape(matrix):
    """return true if rows of matrix have the same len otherwise return false
    :param matrix: (list)
    """

    length_of_first_row = 0
    for i in range(len(matrix)):
        if i == 0:
            length_of_first_row = len(matrix[i])
        if length_of_first_row != len(matrix[i]):
            return False

    return True


if __name__ == "__main__":
    matrix = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    try:
        new_matrix = matrix_divided(matrix, 10)
        print("[")
        for i in range(len(new_matrix)):
            print(" [", end="")
            for j in range(len(new_matrix[i])):
                if j == len(new_matrix[i]) - 1:
                    print(new_matrix[i][j], end="")
                    break
                print(new_matrix[i][j], end=", ")
            print("]", end=",\n")

        print("]")
    except Exception as e:
        print(e)
