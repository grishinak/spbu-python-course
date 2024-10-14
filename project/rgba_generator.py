from typing import Tuple

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
        for a in range(0, 101)
        if a % 2 == 0  # Only even alpha values
    )

    # Retrieve the i-th element from the generator expression
    for idx, rgba in enumerate(rgba_gen):
        if idx == i:
            return rgba
