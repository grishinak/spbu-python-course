import pytest
from project.cache_decorator import cache_results, cache_results_f

# Test for the version without the flag
@cache_results(max_size=3)
def expensive_function(x, y):
    """Example function that simulates long computations."""
    return x + y


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (1, 2, 3),  # First computation, saved to cache
        (1, 2, 3),  # Get from cache
        (2, 3, 5),  # Saved to cache
        (3, 4, 7),  # Saved to cache: cache full now (3, 5, 7)
        (1, 2, 3),  # Get from cache
        (4, 5, 9),  # Added to cache, removes result 3 from cache
        (1, 2, 3),  # New computation, added to cache
    ],
)
def test_cache_expensive_function(x, y, expected):
    """Test to verify caching behavior without flag."""
    result = expensive_function(x, y)
    assert result == expected


# its unnecessary
# Test for the version with the flag
@cache_results_f(max_size=3)
def expensive_function_f(x, y):
    """Example function that simulates long computations (with flag)."""
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
def test_cache_expensive_function_f(x, y, expected, from_cache):
    """Test to verify caching behavior with flag."""
    result, is_cached = expensive_function_f(x, y)
    assert result == expected
    assert is_cached == from_cache
