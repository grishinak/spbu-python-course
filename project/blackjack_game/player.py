from .deck import Deck
from .card import Card

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.balance = 200
        self.bet = 0

    def set_bet(self, amount):
        if amount > self.balance:
            raise ValueError("Bet exceeds balance")
        self.bet = amount

    def adjust_balance(self, amount):
        self.balance += amount

    def add_card(self, card):
        self.hand.append(card)

    def calculate_score(self):
        score = sum(card.value() for card in self.hand)
        aces = sum(1 for card in self.hand if card.rank == "A")
        while score > 21 and aces:
            score -= 10
            aces -= 1
        return score

    def make_move(self, deck):
        while self.calculate_score() < 17:
            self.add_card(deck.draw())
            print(f"{self.name} draws 🎴 {self.hand[-1]}.")


class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer")


class Bot(Player):
    def __init__(self, name):
        super().__init__(name)
