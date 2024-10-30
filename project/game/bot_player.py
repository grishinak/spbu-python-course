import random
from hand import Hand
from card import Deck


class BotPlayer:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def take_turn(self, deck: Deck):
        raise NotImplementedError("This method should be implemented in subclasses")

    def reset_hand(self):
        self.hand = Hand()


class ConservativeBot(BotPlayer):
    def take_turn(self, deck: Deck):
        while self.hand.calculate_score() < 15:
            self.hand.add_card(deck.draw_card())


class AggressiveBot(BotPlayer):
    def take_turn(self, deck: Deck):
        while self.hand.calculate_score() < 18:
            self.hand.add_card(deck.draw_card())


class RandomBot(BotPlayer):
    def take_turn(self, deck: Deck):
        while self.hand.calculate_score() < 21 and random.choice([True, False]):
            self.hand.add_card(deck.draw_card())
