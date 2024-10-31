from .deck import Deck
from .card import Card
from typing import List, Union


class Player:
    def __init__(self, name: str) -> None:
        """
        Initialize a Player instance.

        :param name: The name of the player.
        """
        self.name: str = name
        self.hand: List[Card] = []
        self.balance: int = 200
        self.bet: int = 0

    def set_bet(self, amount: int) -> None:
        """
        Set the player's bet amount.

        :param amount: The bet amount to set.
        :raises ValueError: If the bet exceeds the player's balance.
        """
        if amount > self.balance:
            raise ValueError("Bet exceeds balance")
        self.bet = amount

    def adjust_balance(self, amount: int) -> None:
        """
        Adjust the player's balance.

        :param amount: The amount to adjust the balance by (can be positive or negative).
        """
        self.balance += amount

    def add_card(self, card: Card) -> None:
        """
        Add a card to the player's hand.

        :param card: The Card instance to add to the hand.
        """
        self.hand.append(card)

    def calculate_score(self) -> int:
        """
        Calculate the total score of the player's hand.

        :return: The calculated score, with Aces counted as 1 or 11 as appropriate.
        """
        score: int = sum(card.value() for card in self.hand)
        aces: int = sum(1 for card in self.hand if card.rank == "A")
        while score > 21 and aces:
            score -= 10
            aces -= 1
        return score

    def make_move(self, deck: Deck) -> None:
        """
        Make the player's move by drawing cards until the score is 17 or higher.

        :param deck: The Deck instance to draw cards from.
        """
        while self.calculate_score() < 17:
            self.add_card(deck.draw())
            print(f"{self.name} draws 🎴 {self.hand[-1]}.")


class Dealer(Player):
    def __init__(self) -> None:
        """
        Initialize a Dealer instance.
        """
        super().__init__("Dealer")


class Bot(Player):
    def __init__(self, name: str, strategy: str = "Basic") -> None:
        """
        Initialize a Bot instance with a strategy.

        :param name: The name of the bot.
        :param strategy: The bot's playing strategy.
        """
        super().__init__(name)
        self.strategy = strategy

    def make_move(self, deck: Deck) -> None:
        """
        Make the bot's move based on its strategy.

        :param deck: The Deck instance to draw cards from.
        """
        print(f"{self.name} ({self.strategy}) making a move...")

        # Implement different moves based on strategy
        if self.strategy == "Aggressive":
            while self.calculate_score() < 19:
                self.add_card(deck.draw())
                print(f"{self.name} ({self.strategy}) draws 🎴 {self.hand[-1]}.")
        elif self.strategy == "Conservative":
            while self.calculate_score() < 15:
                self.add_card(deck.draw())
                print(f"{self.name} ({self.strategy}) draws 🎴 {self.hand[-1]}.")
        elif self.strategy == "Risky":
            while self.calculate_score() < 20:
                self.add_card(deck.draw())
                print(f"{self.name} ({self.strategy}) draws 🎴 {self.hand[-1]}.")
        else:  # Default to Basic Strategy
            while self.calculate_score() < 17:
                self.add_card(deck.draw())
                print(f"{self.name} draws 🎴 {self.hand[-1]}.")
