from typing import TYPE_CHECKING

# use to prevent circular imports
if TYPE_CHECKING:
    from player import Bot  
    from deck import Deck   

class Strategy:
    """
    Base class for different strategies that a bot can use in the game.

    :param bot: The bot instance that will make a move.
    :param deck: The deck of cards that the bot draws from.
    """

    def make_move(self, bot: "Bot", deck: "Deck") -> None:
        """
        Abstract method that should be overridden in subclasses to implement the strategy.

        :param bot: The bot instance making the move.
        :param deck: The deck from which cards will be drawn.
        :raises NotImplementedError: If this method is not overridden in a subclass.
        """
        raise NotImplementedError("This method should be overridden in subclasses.")


class AggressiveStrategy(Strategy):
    """
    Aggressive strategy for a bot to keep drawing cards until its score is at least 19.

    :param bot: The bot instance that will make a move.
    :param deck: The deck from which cards will be drawn.
    """
    def make_move(self, bot: "Bot", deck: "Deck") -> None:
        """
        Executes the aggressive strategy: draws cards until the bot's score is at least 19.

        :param bot: The bot instance making the move.
        :param deck: The deck from which cards will be drawn.
        """          
        while bot.calculate_score() < 19:
            bot.add_card(deck.draw())
            print(f"{bot.name} ({self.__class__.__name__}) draws 🎴 {bot.hand[-1]}.")


class ConservativeStrategy(Strategy):
    """
    Conservative strategy for a bot to keep drawing cards until its score is at least 15.

    :param bot: The bot instance that will make a move.
    :param deck: The deck from which cards will be drawn.
    """
    def make_move(self, bot: "Bot", deck: "Deck") -> None:
        """
        Executes the conservative strategy: draws cards until the bot's score is at least 15.

        :param bot: The bot instance making the move.
        :param deck: The deck from which cards will be drawn.
        """    
        while bot.calculate_score() < 15:
            bot.add_card(deck.draw())
            print(f"{bot.name} ({self.__class__.__name__}) draws 🎴 {bot.hand[-1]}.")


class RiskyStrategy(Strategy):
    """
    Risky strategy for a bot to keep drawing cards until its score is at least 20.

    :param bot: The bot instance that will make a move.
    :param deck: The deck from which cards will be drawn.
    """
    def make_move(self, bot: "Bot", deck: "Deck") -> None:
        """
        Executes the risky strategy: draws cards until the bot's score is at least 20.

        :param bot: The bot instance making the move.
        :param deck: The deck from which cards will be drawn.
        """    
        while bot.calculate_score() < 20:
            bot.add_card(deck.draw())
            print(f"{bot.name} ({self.__class__.__name__}) draws 🎴 {bot.hand[-1]}.")


class BasicStrategy(Strategy):
    """
    Basic strategy for a bot to keep drawing cards until its score is at least 17.

    :param bot: The bot instance that will make a move.
    :param deck: The deck from which cards will be drawn.
    """
    def make_move(self, bot: "Bot", deck: "Deck") -> None:
        """
        Executes the basic strategy: draws cards until the bot's score is at least 17.

        :param bot: The bot instance making the move.
        :param deck: The deck from which cards will be drawn.
        """    
        while bot.calculate_score() < 17:
            bot.add_card(deck.draw())
            print(f"{bot.name} ({self.__class__.__name__}) draws 🎴 {bot.hand[-1]}.")


class AdaptiveStrategy(Strategy):
    """
    Adaptive strategy that adjusts the bot's behavior based on previous round results.

    :param bot: The bot instance that will make a move.
    :param deck: The deck from which cards will be drawn.
    """
    def make_move(self, bot: "Bot", deck: "Deck") -> None:
        """
        Adjusts the bot's strategy based on the results of the previous round and bet.

        :param bot: The bot instance making the move.
        :param deck: The deck from which cards will be drawn.
        """
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

    def play_aggressive(self, bot: "Bot", deck: "Deck") -> None:
        """
        Executes the aggressive strategy: draws cards until the bot's score is at least 19.

        :param bot: The bot instance making the move.
        :param deck: The deck from which cards will be drawn.
        """
        while bot.calculate_score() < 19:
            bot.add_card(deck.draw())
            print(f"{bot.name} (Aggressive) draws 🎴 {bot.hand[-1]}.")

    def play_conservative(self, bot: "Bot", deck: "Deck") -> None:
        """
        Executes the conservative strategy: draws cards until the bot's score is at least 15.

        :param bot: The bot instance making the move.
        :param deck: The deck from which cards will be drawn.
        """
        while bot.calculate_score() < 15:
            bot.add_card(deck.draw())
            print(f"{bot.name} (Conservative) draws 🎴 {bot.hand[-1]}.")

    def play_basic(self, bot: "Bot", deck: "Deck") -> None:
        """
        Executes the basic strategy: draws cards until the bot's score is at least 17.

        :param bot: The bot instance making the move.
        :param deck: The deck from which cards will be drawn.
        """    
        while bot.calculate_score() < 17:
            bot.add_card(deck.draw())
            print(f"{bot.name} (Basic) draws 🎴 {bot.hand[-1]}.")
