from .deck import Deck
from .card import Card
from typing import List, TypedDict
from .strategy import Strategy


class HistoryDict(TypedDict):
    """
    Typed dictionary for storing the betting history of a bot player in Blackjack.

    :param bets (List[int]): A list of integers representing the amounts bet by the player in each round.
    :param results (List[str]): A list of strings representing the outcome of each round ("win", "lose", or "tie").
    """

    bets: List[int]
    results: List[str]


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
    def __init__(self, name: str, strategy: Strategy) -> None:
        """
        Initialize a Bot instance.
        """
        super().__init__(name)
        self.strategy = strategy
        # Define history with clear types for bets and results
        self.history: HistoryDict = {
            "bets": [],  # List of bet amounts (integers)
            "results": [],  # List of game results (strings: "win", "lose", "tie")
        }

    def add_history(self, bet: int, result: str) -> None:
        """
        Add bet and result information to the history for the current round.

        :param bet: The bet amount.
        :param result: The result of the game (win, lose, tie).
        """
        self.history["bets"].append(bet)
        self.history["results"].append(result)

    def make_move(self, deck: Deck) -> None:
        """
        Make a move based on the current strategy.
        """
        self.strategy.make_move(self, deck)
