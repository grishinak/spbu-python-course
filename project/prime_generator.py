from typing import Generator, Callable, List, Union


def prime_number_generator() -> Generator[int, None, None]:
    """
    Generator of prime numbers.

    Yields
    ------
    int
        The next prime number in the sequence.
    """
    number = 2
    primes: List[int] = []
    while True:
        if all(number % p != 0 for p in primes):
            primes.append(number)
            yield number
        number += 1


def get_kth_prime(
    func: Callable[[], Generator[int, None, None]]
) -> Callable[[int], int]:
    """
    Decorator to get the k-th prime number from a prime generator.

    Parameters
    ----------
    func : Callable
        A function that returns a generator of prime numbers.

    Returns
    -------
    Callable[[int], int]
        A function that returns the k-th prime number.
    """

    def wrapper(k: int) -> int:
        """
        Get the k-th prime number.

        Parameters
        ----------
        k : int
            The index of the prime number to return (1-based).

        Returns
        -------
        int
            The k-th prime number.
        """
        prime_gen = func()
        prime: Union[int, None] = None
        for _ in range(k):
            prime = next(prime_gen)
        assert prime is not None, "Prime generator returned None unexpectedly"
        return prime

    return wrapper


# wrap the func here
@get_kth_prime
def kth_prime_generator() -> Generator[int, None, None]:  # renamed due mypy redef error
    """
    Generator of prime numbers with a decorator to get the k-th prime number.

    Yields
    ------
    int
        The next prime number in the sequence.
    """
    number = 2
    primes: List[int] = []
    while True:
        if all(number % p != 0 for p in primes):
            primes.append(number)
            yield number
        number += 1
