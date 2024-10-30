import pytest
from project.generators.prime_generator import (
    prime_number_generator,
    get_kth_prime,
)

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


## test func-gen which wrapped here
@pytest.mark.parametrize(
    "k, expected_prime",
    [
        (1, 2),
        (2, 3),
        (3, 5),
        (4, 7),
        (5, 11),
        (6, 13),
    ],
)
def test_get_kth_prime(k, expected_prime):
    """Testing the prime_number_generator function with decorator to obtain the kth prime number."""

    @get_kth_prime
    def prime_gen():
        return prime_number_generator()

    assert prime_gen(k) == expected_prime
