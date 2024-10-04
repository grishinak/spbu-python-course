from typing import Tuple, Iterator


def rgba_generator() -> Iterator[Tuple[int, int, int, int]]:
    """Generate RGBA color vectors.

    Generates four-dimensional color vectors in the RGBA model, where
    each component (R, G, B) takes values from 0 to 255, and the
    alpha (A) component takes even values from 0 to 100.

    Yields
    -------
    Tuple[int, int, int, int]
        A four-dimensional color vector in the format (R, G, B, A).

    Examples
    ---------
    >>> generator = rgba_generator()
    >>> next(generator)
    (0, 0, 0, 0)
    >>> next(generator)
    (0, 0, 0, 2)
    """
    for r in range(256):
        for g in range(256):
            for b in range(256):
                for a in range(0, 100, 2):
                    yield (r, g, b, a)


def get_rgba_element(i: int) -> Tuple[int, int, int, int]:
    """Retrieve the i-th element from the RGBA set.

    Gets the i-th RGBA vector from the total set of vectors
    generated by the `rgba_generator`. Indexing starts at 0.

    Parameters
    ----------
    i : int
        The index of the vector to retrieve.

    Returns
    -------
    Tuple[int, int, int, int]
        A four-dimensional color vector in the format (R, G, B, A).

    Raises
    ------
    IndexError
        If the index is out of the valid range.

    Examples
    ---------
    >>> get_rgba_element(0)
    (0, 0, 0, 0)
    >>> get_rgba_element(1)
    (0, 0, 0, 2)
    """
    total_colors = 256
    total_alpha = 51
    total_combinations = total_colors**3 + total_alpha
    if i < 0 or i >= total_combinations:
        raise IndexError("Index out of range.")

    gen = rgba_generator()
    for _ in range(i):
        next(gen)
    return next(gen)
