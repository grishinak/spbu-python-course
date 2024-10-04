from typing import Tuple, Iterator


def rgba_generator() -> Iterator[Tuple[int, int, int, int]]:
    for r in range(256):
        for g in range(256):
            for b in range(256):
                for a in range(0, 100, 2):
                    yield (r, g, b, a)


def get_rgba_element(i: int) -> Tuple[int, int, int, int]:

    total_colors = 256
    total_alpha = 51
    total_combinations = total_colors**3 + total_alpha
    if i < 0 or i >= total_combinations:
        raise IndexError("Index out of range.")

    gen = rgba_generator()
    for _ in range(i):
        next(gen)
    return next(gen)
