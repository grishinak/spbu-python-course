from .card import Card, Suit
import random
from typing import List


class Deck:
    def __init__(self) -> None:
        """
        Initializes a Deck of 52 playing cards, shuffling them upon creation.

        This deck contains cards of all ranks and suits:
        - Ranks: 2 through 10, J, Q, K, A
        - Suits: SPADES, HEARTS, DIAMONDS, CLUBS
        """
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = [Suit.SPADES, Suit.HEARTS, Suit.DIAMONDS, Suit.CLUBS]
        self._cards: List[Card] = [Card(rank, suit) for rank in ranks for suit in suits]
        random.shuffle(self._cards)

    def draw(self) -> Card:
        """
        Draws a card from the deck.

        :return: A Card object representing the drawn card.
        :raises IndexError: If the deck is empty.
        """
        if not self._cards:
            raise IndexError("The deck is empty")
        return self._cards.pop()
