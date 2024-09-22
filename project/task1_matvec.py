from math import sqrt, acos, degrees
from typing import List

# 1.Vector operations[]


def dot_product(v1: List[float], v2: List[float]) -> float:
    """
    Calculate the dot product of two vectors.

    Parameters
    ----------
    v1 : List[float]
        The first input vector.
    v2 : List[float]
        The second input vector.

    Returns
    -------
    float
        The dot product of the two vectors.

    Raises
    ------
    ValueError
        If the lengths of the input vectors are not equal.
    """
    if len(v1) != len(v2):
        raise ValueError("Error: vector lengths are not equal.")

    dot_product = 0.0
    for i in range(len(v1)):
        dot_product += v1[i] * v2[i]

    return dot_product


def vector_length(v: List[float]) -> float:
    """
    Calculate the length of a vector.

    Parameters
    ----------
    v : List[float]
        The input vector.

    Returns
    -------
    float
        The length of the vector.
    """
    total = 0.0
    for i in range(len(v)):
        total += (v[i]) ** 2

    return sqrt(total)


def angle(v1: List[float], v2: List[float]) -> float:
    """
    Calculate the angle between two vectors in degrees.

    Parameters
    ----------
    v1 : List[float]
        The first input vector.
    v2 : List[float]
        The second input vector.

    Returns
    -------
    float
        The angle between the two vectors in degrees.
    """
    return degrees(acos(dot_product(v1, v2) / (vector_length(v1) * vector_length(v2))))


# 2.Matrix operations [ [][]...[] ]


def matrix_addition(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
    """
    Add two matrices.

    Parameters
    ----------
    A : List[List[float]]
        The first input matrix.
    B : List[List[float]]
        The second input matrix.

    Returns
    -------
    List[List[float]]
        The resulting matrix from the addition.

    Raises
    ------
    ValueError
        If the dimensions of the input matrices do not match.
    """
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Error: matrices of different dimensions.")

    result_m = [[0.0] * len(A[0]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            result_m[i][j] = A[i][j] + B[i][j]
    return result_m


def matrix_multiplication(
    A: List[List[float]], B: List[List[float]]
) -> List[List[float]]:
    """
    Multiply two matrices.

    Parameters
    ----------
    A : List[List[float]]
        The first input matrix.
    B : List[List[float]]
        The second input matrix.

    Returns
    -------
    List[List[float]]
        The resulting matrix from the multiplication.

    Raises
    ------
    ValueError
        If the number of columns in the first matrix does not match
        the number of rows in the second matrix.

    Examples
    --------
    >>> matrix_multiplication([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    [[19, 22], [43, 50]]
    """
    if len(A[0]) != len(B):
        raise ValueError(
            "Error: number of rows of first matrix and number of columns of second matrix are different."
        )

    result_m = [[0.0] * len(B[0]) for i in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result_m[i][j] += A[i][k] * B[k][j]

    return result_m


def matrix_transpose(A: List[List[float]]) -> List[List[float]]:
    """
    Transpose a matrix.

    Parameters
    ----------
    A : List[List[float]]
        The input matrix to be transposed.

    Returns
    -------
    List[List[float]]
        The transposed matrix.
    """

    result_m = [[0.0] * len(A) for i in range(len(A[0]))]

    for i in range(len(A[0])):
        for j in range(len(A)):
            result_m[i][j] = A[j][i]
    return result_m
