from typing import Tuple #, Iterator

# 1. generator-expression

def get_rgba_element(i: int) -> Tuple[int, int, int, int]:
    """Returns the i-th element from the RGBA vector generator.

    Parameters
    ----------
    i : int
        Index of the element to return.

    Returns
    -------
    Tuple[int, int, int, int]
        The i-th RGBA vector in the format (R, G, B, A).

    Raises
    ------
    IndexError
        If the index is out of range.
    """
    total_colors = 256
    total_alpha = 51
    total_combinations = total_colors**3 * total_alpha

    if i < 0 or i >= total_combinations:
        raise IndexError("Index out of range.")

    # Using a generator expression directly in the function
    rgba_gen = (
        (r, g, b, a)
        for r in range(total_colors)
        for g in range(total_colors)
        for b in range(total_colors)
        for a in range(0, 101, 2)  # Only even alpha values
    )

    # Retrieve the i-th element from the generator expression
    for idx, rgba in enumerate(rgba_gen):
        if idx == i:
            return rgba



# 2.generator-function (done it first, then realised it is not fit the criteria)

# def rgba_generator() -> Iterator[Tuple[int, int, int, int]]:
#     """Generate RGBA color vectors.

#     Generates four-dimensional color vectors in the RGBA model, where
#     each component (R, G, B) takes values from 0 to 255, and the
#     alpha (A) component takes even values from 0 to 100.

#     Yields
#     -------
#     Tuple[int, int, int, int]
#         A four-dimensional color vector in the format (R, G, B, A).

#     Examples
#     ---------
#     >>> generator = rgba_generator()
#     >>> next(generator)
#     (0, 0, 0, 0)
#     >>> next(generator)
#     (0, 0, 0, 2)
#     """
#     for r in range(256):
#         for g in range(256):
#             for b in range(256):
#                 for a in range(0, 101, 2):
#                     yield (r, g, b, a)


# def get_rgba_element(i: int) -> Tuple[int, int, int, int]:
#     """Retrieve the i-th element from the RGBA set.

#     Gets the i-th RGBA vector from the total set of vectors
#     generated by the `rgba_generator`. Indexing starts at 0.

#     Parameters
#     ----------
#     i : int
#         The index of the vector to retrieve.

#     Returns
#     -------
#     Tuple[int, int, int, int]
#         A four-dimensional color vector in the format (R, G, B, A).

#     Raises
#     ------
#     IndexError
#         If the index is out of the valid range.

#     Examples
#     ---------
#     >>> get_rgba_element(0)
#     (0, 0, 0, 0)
#     >>> get_rgba_element(1)
#     (0, 0, 0, 2)
#     """
#     total_colors = 256
#     total_alpha = 51
#     total_combinations = total_colors**3 * total_alpha
#     if i < 0 or i >= total_combinations:
#         raise IndexError("Index out of range.")

#     gen = rgba_generator()
#     for _ in range(i):
#         next(gen)
#     return next(gen)
