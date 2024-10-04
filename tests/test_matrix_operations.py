import pytest
from project.matrix_operations import (
    matrix_addition,
    matrix_multiplication,
    matrix_transpose,
)

# Tests for matrix operations


def test_matrix_addition():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    assert matrix_addition(A, B) == [[6, 8], [10, 12]]

    # A test for incorrect matrix sizes
    with pytest.raises(ValueError):
        matrix_addition([[1]], [[1, 2]])

    # A test with zero elements
    A = [[0, 0], [0, 0]]
    B = [[1, 2], [3, 4]]
    assert matrix_addition(A, B) == [[1, 2], [3, 4]]


def test_matrix_multiplication():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    assert matrix_multiplication(A, B) == [[19, 22], [43, 50]]

    # A test for incorrect matrix sizes
    with pytest.raises(ValueError):
        matrix_multiplication([[1, 2]], [[1], [2], [3]])

    # Multiplication by a identity matrix
    A = [[1, 2], [3, 4]]
    E = [[1, 0], [0, 1]]
    assert matrix_multiplication(A, E) == A

    # A test with zero elements
    A = [[0, 0], [0, 0]]
    B = [[1, 2], [3, 4]]
    assert matrix_multiplication(A, B) == [[0, 0], [0, 0]]

    # Multiplication of 3x2 and 2x3 matrices
    A = [[1, 2], [3, 4], [5, 6]]
    B = [[7, 8, 9], [10, 11, 12]]
    assert matrix_multiplication(A, B) == [[27, 30, 33], [61, 68, 75], [95, 106, 117]]

    # A test for multiplying a 1x2 matrix by 2x1
    A = [[1, 2]]
    B = [[3], [4]]
    assert matrix_multiplication(A, B) == [[11]]


def test_matrix_transpose():
    A = [[1, 2, 3], [4, 5, 6]]
    assert matrix_transpose(A) == [[1, 4], [2, 5], [3, 6]]

    # The Square matrix test
    B = [[1, 2], [3, 4]]
    assert matrix_transpose(B) == [[1, 3], [2, 4]]
