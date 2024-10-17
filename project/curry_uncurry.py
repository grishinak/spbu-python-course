from typing import Callable, Any


def curry_explicit(func: Callable[..., Any], arity: int) -> Callable[..., Any]:
    """
    Curry a function to accept one argument at a time, returning a function that takes
    subsequent arguments until the total number of arguments equals the arity.

    Parameters
    ----------
    func : callable
        The function to be curried.
    arity : int
        The number of arguments the original function expects.

    Returns
    -------
    curried_func : callable
        A curried version of the original function.

    Raises
    ------
    ValueError
        If arity is not a non-negative integer.
    TypeError
        If too many arguments are provided when calling the curried function.

    Examples
    --------
    >>> f2 = curry_explicit(lambda x, y, z: f'<{x}, {y}, {z}>', 3)
    >>> f2(1)(2)(3)
    '<1, 2, 3>'
    """
    if not isinstance(arity, int) or arity < 0:
        raise ValueError("Arity must be a non-negative integer.")

    def curried(*args: Any) -> Any:
        if len(args) > arity:
            raise TypeError(
                f"Too many arguments: expected at most {arity}, got {len(args)}."
            )

        # If there are enough arguments, we call the original function
        if len(args) == arity:
            return func(*args)

        # Returning a new function for next arguments
        return lambda *more_args: curried(*(args + more_args))

    return curried


def uncurry_explicit(curry_func: Callable[..., Any], arity: int) -> Callable[..., Any]:
    """
    Uncurry a curried function so that it can accept all arguments at once.

    Parameters
    ----------
    curry_func : callable
        The curried function to be uncurried.
    arity : int
        The number of arguments the original function expects.

    Returns
    -------
    uncurried_func : callable
        The uncurried version of the function.

    Raises
    ------
    ValueError
        If arity is not a non-negative integer.
    TypeError
        If the number of arguments provided does not match the arity.

    Examples
    --------
    >>> f2 = curry_explicit(lambda x, y, z: f'<{x}, {y}, {z}>', 3)
    >>> g2 = uncurry_explicit(f2, 3)
    >>> g2(1, 2, 3)
    '<1, 2, 3>'
    """
    if not isinstance(arity, int) or arity < 0:
        raise ValueError("Arity must be a non-negative integer.")

    def uncurried(*args: Any) -> Any:
        if len(args) != arity:
            raise TypeError(f"Expected exactly {arity} arguments, but got {len(args)}.")

        return curry_func(*args)

    return uncurried
