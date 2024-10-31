import random
from typing import List
from .card import Card


class Deck:
    def __init__(self) -> None:
        """
        Initializes a Deck of 52 playing cards, shuffling them upon creation.

        This deck contains cards of all ranks and suits:
        - Ranks: 2 through 10, J, Q, K, A
        - Suits: ♠️, ♥️, ♦️, ♣️
        """
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["♠️", "♥️", "♦️", "♣️"]
        self.cards: List[Card] = [Card(rank, suit) for rank in ranks for suit in suits]
        random.shuffle(self.cards)

    def draw(self) -> Card:
        """
        Draws a card from the deck.

        :return: A Card object representing the drawn card.
        :raises IndexError: If the deck is empty.
        """
        return self.cards.pop()
