import random


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def value(self):
        if self.rank in ["J", "Q", "K"]:
            return 10
        elif self.rank == "A":
            return 11  # Обработаем ас отдельно в Hand
        else:
            return int(self.rank)

    def __repr__(self):
        return f"{self.rank}{self.suit}"


class Deck:
    suits = ["♠", "♣", "♥", "♦"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in Deck.suits for rank in Deck.ranks]
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()
