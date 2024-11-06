from .deck import Deck
from .card import Card
from typing import List

# strategies(replace to another file?)
class Strategy:
    def make_move(self, bot: "Bot", deck: Deck) -> None:
        raise NotImplementedError("This method should be overridden in subclasses.")


class AggressiveStrategy(Strategy):
    def make_move(self, bot: "Bot", deck: Deck) -> None:
        while bot.calculate_score() < 19:
            bot.add_card(deck.draw())
            print(
                f"{bot.name} ({bot.strategy.__class__.__name__}) draws 🎴 {bot.hand[-1]}."
            )


class ConservativeStrategy(Strategy):
    def make_move(self, bot: "Bot", deck: Deck) -> None:
        while bot.calculate_score() < 15:
            bot.add_card(deck.draw())
            print(
                f"{bot.name} ({bot.strategy.__class__.__name__}) draws 🎴 {bot.hand[-1]}."
            )


class RiskyStrategy(Strategy):
    def make_move(self, bot: "Bot", deck: Deck) -> None:
        while bot.calculate_score() < 20:
            bot.add_card(deck.draw())
            print(
                f"{bot.name} ({bot.strategy.__class__.__name__}) draws 🎴 {bot.hand[-1]}."
            )


class BasicStrategy(Strategy):
    def make_move(self, bot: "Bot", deck: Deck) -> None:
        while bot.calculate_score() < 17:
            bot.add_card(deck.draw())
            print(
                f"{bot.name} ({bot.strategy.__class__.__name__}) draws 🎴 {bot.hand[-1]}."
            )


class AdaptiveStrategy(Strategy):
    def make_move(self, bot: "Bot", deck: Deck) -> None:
        # will use the results of the last rounds
        if len(bot.history["results"]) > 0:
            last_result = bot.history["results"][-1]
            last_bet = bot.history["bets"][-1]

            if last_result == "lose":
                print(f"{bot.name} is playing more conservatively after a loss.")
                self.play_conservative(bot, deck)
            elif last_result == "win" and last_bet > 50:
                print(f"{bot.name} is playing aggressively after a big win.")
                self.play_aggressive(bot, deck)
            else:
                print(f"{bot.name} is following a basic strategy.")
                self.play_basic(bot, deck)
        else:
            print(f"{bot.name} has no history, using basic strategy.")
            self.play_basic(bot, deck)

    def play_aggressive(self, bot: "Bot", deck: Deck) -> None:
        """
        Play aggressively: pull the cards until the amount is 19 or more.
        """
        while bot.calculate_score() < 19:
            bot.add_card(deck.draw())
            print(f"{bot.name} (Aggressive) draws 🎴 {bot.hand[-1]}.")

    def play_conservative(self, bot: "Bot", deck: Deck) -> None:
        """
        Play carefully: pull the cards until the amount is 15 or more.
        """
        while bot.calculate_score() < 15:
            bot.add_card(deck.draw())
            print(f"{bot.name} (Conservative) draws 🎴 {bot.hand[-1]}.")

    def play_basic(self, bot: "Bot", deck: Deck) -> None:
        """
        The standard strategy is to pull the cards until the amount is 17 or more.
        """
        while bot.calculate_score() < 17:
            bot.add_card(deck.draw())
            print(f"{bot.name} (Basic) draws 🎴 {bot.hand[-1]}.")


# main player class


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
        super().__init__(name)
        self.strategy = strategy
        self.history = {
            "bets": [],
            "results": [],  # History of results (win, lose, tie) for each round
        }

    def add_history(self, bet: int, result: str) -> None:
        """
        Adds information about the bet and the result to the history for the current round.
        :param bet: The amount of the bet.
        :param result: game result (win, lose, tie).
        """
        self.history["bets"].append(bet)
        self.history["results"].append(result)

    def make_move(self, deck: Deck) -> None:
        """
        Performs a move based on the current strategy.
        """
        self.strategy.make_move(self, deck)
