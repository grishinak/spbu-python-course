from math import sqrt, acos, degrees
from typing import List

# Vector operations


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
