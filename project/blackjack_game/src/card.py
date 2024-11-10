from enum import Enum


class Suit(Enum):
    SPADES = "♠️"
    HEARTS = "♥️"
    DIAMONDS = "♦️"
    CLUBS = "♣️"

    def __str__(self):
        return self.value


class Card:
    def __init__(self, rank: str, suit: Suit) -> None:
        """
        Initializes a card object.

        :param rank: The rank of the card (e.g., "A", "K", "4", "7").
        :param suit: The suit of the card (e.g., Suit.SPADES, Suit.HEARTS).
        """
        self._rank = rank
        self._suit = suit

    def value(self) -> int:
        """
        Returns the blackjack value of the card.
        Face cards (J, Q, K) count as 10, and an Ace (A) counts as 11.

        :return: The value of the card for blackjack.
        """
        if self._rank in ["J", "Q", "K"]:
            return 10
        elif self._rank == "A":
            return 11
        else:
            return int(self._rank)

    def __str__(self) -> str:
        """
        Returns a string representation of the card in the format "Rank Suit".

        :return: A string representing the card.
        """
        return f"{self._rank} {self._suit}"
