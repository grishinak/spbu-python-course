from typing import Generator, Callable


def prime_number_generator() -> Generator[int, None, None]:
    """
    Generator of prime numbers.

    Yields
    ------
    int
        The next prime number in the sequence.
    """
    # O(sqrt(N))
    number = 2
    while True:
        is_prime = True
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            yield number
        number += 1


def get_kth_prime(
    func: Callable[[], Generator[int, None, None]]
) -> Callable[[int], int]:
    """
    Decorator to get the k-th prime number from a prime generator.

    Parameters
    ----------
    func : Callable[[], Generator[int, None, None]]
        A function that returns a generator of prime numbers.

    Returns
    -------
    Callable[[int], int]
        A function that returns the k-th prime number.
    """
    # Create a prime number generator once
    prime_gen = func()

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
        prime: int = 0
        for _ in range(k):
            prime = next(prime_gen)
        return prime

    return wrapper
