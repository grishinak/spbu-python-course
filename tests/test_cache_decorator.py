import pytest
from project.cache_decorator import cache_results


@cache_results(max_size=3)
def expensive_function(x, y):
    """Example function that simulates long computations."""
    return x + y


@pytest.mark.parametrize(
    "x, y, expected, from_cache",
    [
        (1, 2, 3, False),  # First computation, saved to cache
        (1, 2, 3, True),  # Get from cache
        (2, 3, 5, False),  # Saved to cache
        (3, 4, 7, False),  # Saved to cache: cache full now (3, 5, 7)
        (1, 2, 3, True),  # Get from cache
        (4, 5, 9, False),  # Added to cache, removes result 3 from cache
        (1, 2, 3, False),  # New computation, added to cache
    ],
)
def test_cache_expensive_function(x, y, expected, from_cache):
    """Test to verify caching behavior."""
    result, is_cached = expensive_function(x, y)
    assert result == expected
    assert (
        is_cached == from_cache
    )  # Verify whether the result was Get from cache by Flag
