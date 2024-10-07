from typing import Callable


def curry_explicit(function: Callable, arity: int) -> Callable:
    if arity < 0:
        raise ValueError("Arity cannot be negative.")

    def curried(*args):
        if len(args) > arity:
            raise TypeError(
                f"Function expected at most {arity} arguments, got {len(args)}."
            )
        if len(args) == arity:
            return function(*args)
        return lambda *more_args: curried(*(args + more_args))

    return curried


def uncurry_explicit(function: Callable, arity: int) -> Callable:
    if arity < 0:
        raise ValueError("Arity cannot be negative.")

    def uncurried(*args):
        if len(args) != arity:
            raise TypeError(f"Function expected {arity} arguments, got {len(args)}.")
        return function(*args)

    return uncurried
