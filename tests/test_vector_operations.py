import pytest
from project.vector_oprations import (
    dot_product,
    vector_length,
    angle,
)

# Tests for vector operations


def test_dot_product():
    assert dot_product([1, 2, 3], [4, 5, 6]) == 32.0

    # Zero Vector test
    assert dot_product([0, 0, 0], [1, 1, 1]) == 0.0

    # Vectors with negative numbers
    assert dot_product([1, -2, 3], [-4, 5, -6]) == -32.0

    # Vector size mismatch
    with pytest.raises(ValueError):
        dot_product([1, 2], [1])


def test_vector_length():
    assert vector_length([3, 4]) == pytest.approx(5.0)
    assert vector_length([1, 0, 0]) == 1.0
    assert vector_length([0, 0, 0]) == 0.0

    # A vector with negative components
    assert vector_length([-3, -4]) == pytest.approx(5.0)


def test_angle():
    # Orthogonal vectors
    assert pytest.approx(angle([1, 0], [0, 1]), 0.1) == 90.0
    assert pytest.approx(angle([0, 1], [1, 0]), 0.1) == 90.0
    assert pytest.approx(angle([0, 10], [10, 0]), 0.1) == 90.0

    # Parallel vectors
    assert pytest.approx(angle([1, 0], [1, 0]), 0.1) == 0.0
    assert pytest.approx(angle([1, 0], [-1, 0]), 0.1) == 180.0
