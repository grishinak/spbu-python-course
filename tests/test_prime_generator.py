import pytest
from project.prime_generator import prime_number_generator, kth_prime_generator

# test prime_number_generator
@pytest.mark.parametrize(
    "num_primes, expected_primes",
    [
        (10, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]),
        (5, [2, 3, 5, 7, 11]),
        (0, []),  # check the case when we dont request prime numbers
    ],
)
def test_prime_number_generator(num_primes, expected_primes):
    """Testing a prime number generator."""
    prime_gen = prime_number_generator()
    primes = [next(prime_gen) for _ in range(num_primes)]
    assert primes == expected_primes


# test prime_gen with get_kth_prime decorator
@pytest.mark.parametrize(
    "k, expected",
    [
        (1, 2),
        (2, 3),
        (3, 5),
        (4, 7),
        (5, 11),
        (6, 13),
        (7, 17),
    ],
)
def test_kth_prime_generator(k, expected):
    """Testing the kth_prime_generator function to obtain the kth prime number."""
    assert kth_prime_generator(k) == expected
