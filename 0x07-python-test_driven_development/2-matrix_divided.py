#!/usr/bin/python3
""" This is a matrix module """


def matrix_divided(matrix, div):
    """Divides a 2D matrix by a number.

        Args:
            matrix (list): A 2D matrix where each row has
            the same number of elements.
            div (int or float): The number to divide
            each element of the matrix by.

        Raises:
            TypeError: If matrix is not a list of lists.
            TypeError: If any row of the matrix has a different
            size than the others.

            TypeError: If div is not a number.
            ZeroDivisionError: If div is zero.

        Returns:
            A new 2D matrix with the same dimensions as the
            original matrix, where each element
            is the result of dividing the corresponding
            element in the original matrix by div.
        """
    if not isinstance(matrix, list) and \
    not all(isinstance(elem, list) for elem in matrix):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    size = len(matrix[0])

    new_matrix = [[matrix[j][i] for i in range(size)]
                  for j in range(len(matrix))]

    for i in range(len(matrix)):
        if len(matrix[i]) != size:
            raise TypeError(
                    "Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in new_matrix:
        i = 0
        for elem in row:
            row[i] = row[i] / div
            row[i] = round(row[i], 2)
            i += 1
    return new_matrix
