from copy import deepcopy
from inspect import signature
from typing import Any, Callable


class Isolated:
    """
    Marker class for arguments that should be deep-copied on each function call.

    Use this class when you want to ensure that mutable default arguments do not
    affect subsequent calls to the function. Each time the function is called,
    the argument will be deep-copied, preventing mutation across calls.
    """

    pass


class Evaluated:
    """
    Wrapper class to defer evaluation of a function until accessed.

    This class wraps a callable and ensures that its value is computed only
    when accessed, providing lazy evaluation. It is not compatible with
    `Isolated`. If combined, it raises an exception.

    Parameters
    ----------
    func : callable
        The function to be evaluated when accessed.

    Raises
    ------
    TypeError
        If `Evaluated` is used together with `Isolated`.
    """

    def __init__(self, func: Callable[..., Any]) -> None:
        if isinstance(func, Isolated):
            raise TypeError("Evaluated cannot be used with Isolated.")
        self.func = func

    def get_value(self) -> Any:
        """
        Executes the wrapped function and returns its result.

        Returns
        -------
        Any
            The result of the evaluated function.
        """
        return self.func()


def smart_args(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator to process special argument types like Isolated and Evaluated.

    This decorator processes arguments before passing them to the wrapped function.
    If an argument is marked with `Isolated`, it is deep-copied on each function
    call. If marked with `Evaluated`, the corresponding function is evaluated at
    call time unless an explicit value is provided by the user.

    Parameters
    ----------
    func : callable
        The function to decorate.

    Returns
    -------
    callable
        A decorated function with special argument handling for `Isolated` and `Evaluated`.
    """

    func_sig = signature(func)

    def wrapper(**kwargs: Any) -> Any:
        """
        Modifies input arguments before passing them to the original function.

        Isolated instances are deep-copied, and Evaluated instances are evaluated if no
        value is provided by the user for the corresponding argument.

        Parameters
        ----------
        **kwargs : dict
            The keyword arguments passed to the decorated function.

        Returns
        -------
        Any
            The result of calling the original function with modified arguments.
        """

        for arg_name, param in func_sig.parameters.items():
            if isinstance(param.default, Isolated) and arg_name in kwargs:
                kwargs[arg_name] = deepcopy(kwargs[arg_name])
            elif isinstance(param.default, Evaluated) and arg_name not in kwargs:
                kwargs[arg_name] = param.default.get_value()

        return func(**kwargs)

    return wrapper
