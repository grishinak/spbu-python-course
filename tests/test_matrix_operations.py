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
    with pytest.raises(ValueError):
        matrix_addition([[1]], [[1, 2]])


def test_matrix_multiplication():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    assert matrix_multiplication(A, B) == [[19, 22], [43, 50]]
    with pytest.raises(ValueError):
        matrix_multiplication([[1, 2]], [[1], [2], [3]])


def test_matrix_transpose():
    A = [[1, 2, 3], [4, 5, 6]]
    assert matrix_transpose(A) == [[1, 4], [2, 5], [3, 6]]
    B = [[1, 2], [3, 4], [5, 6]]
    assert matrix_transpose(B) == [[1, 3, 5], [2, 4, 6]]
