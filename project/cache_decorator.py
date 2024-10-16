from collections import OrderedDict
from functools import wraps
from typing import Callable, Tuple, Any

# Added flags to know its computed or not


def cache_results(max_size: int = 0) -> Callable:
    """Decorator for caching the results of a function.

    Parameters
    ----------
    max_size : int
        Maximum number of cached results. Defaults to 0 (no caching).
    """

    def decorator(func: Callable) -> Callable:
        cache: OrderedDict[Tuple, Any] = OrderedDict()

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Tuple[Any, bool]:
            key = (args, frozenset(kwargs.items()))
            if key in cache:
                return cache[key], True  # Return cached result and cache flag

            result = func(*args, **kwargs)  # Compute the result
            cache[key] = result  # Store result in cache

            # Remove old entries if the cache exceeds max_size
            if max_size > 0 and len(cache) > max_size:
                cache.popitem(last=False)  # Remove the oldest entry (FI-FO)

            return (
                result,
                False,
            )  # Return the result and flag indicating it's a new computation

        return wrapper

    return decorator
