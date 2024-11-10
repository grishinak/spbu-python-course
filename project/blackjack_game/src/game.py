import random
from .deck import Deck
from .player import Bot, Dealer
from .strategy import (
    AggressiveStrategy,
    ConservativeStrategy,
    RiskyStrategy,
    BasicStrategy,
    AdaptiveStrategy,
)
from typing import List


class Game:
    def __init__(self, num_bots: int = 3, rounds: int = 5) -> None:
        """
        Initializes a game of Blackjack with a specified number of bots and rounds.
        """
        self._deck = Deck()
        strategies = [
            AggressiveStrategy(),
            ConservativeStrategy(),
            AdaptiveStrategy(),
            RiskyStrategy(),
            BasicStrategy(),
        ]

        self._players: List[Bot] = [
            Bot(f"Bot {i + 1}", strategy=strategies[i % len(strategies)])
            for i in range(num_bots)
        ]

        self._dealer = Dealer()
        self._rounds = rounds
        self._current_round = 0

    def _set_bets(self) -> None:
        """
        Sets bets for all players by randomly selecting a bet amount
        within the player's balance.
        """
        for player in self._players:
            bet = random.randint(1, min(100, player._balance))
            player.set_bet(bet)
            print(f"{player.name} bets 💰 {player._bet}")

    def _deal_initial_cards(self) -> None:
        """
        Deals two initial cards to each player and the dealer.
        """
        for player in self._players:
            player._hand = [self._deck.draw(), self._deck.draw()]
        self._dealer._hand = [self._deck.draw(), self._deck.draw()]

    def _show_hands(self) -> None:
        """
        Displays the hands and scores of all players and the dealer.
        """
        for player in self._players:
            print(
                f"{player.name} 🃏 hand: {', '.join(map(str, player._hand))}, "
                f"Score: {player.calculate_score()} 💰 Bet: {player._bet}, Balance: {player._balance}"
            )
        print(
            f"Dealer 🃏 hand: {', '.join(map(str, self._dealer._hand))}, "
            f"Score: {self._dealer.calculate_score()}"
        )

    def _play_round(self) -> None:
        """
        Plays a single round of Blackjack, including setting bets, dealing cards,
        allowing players to make moves, and determining the winner.
        """
        print(f"\n🎲 Round {self._current_round + 1} 🎲")
        self._set_bets()
        self._deal_initial_cards()
        self._show_hands()

        for player in self._players:
            player.make_move(self._deck)
            print(f"{player.name} ends with score {player.calculate_score()}")

        while self._dealer.calculate_score() < 17:
            self._dealer.make_move(self._deck)
        print(f"Dealer ends with score {self._dealer.calculate_score()}")

        self._determine_winner()

    def _determine_winner(self) -> None:
        """
        Determines the winner of the round based on the scores of the players
        and the dealer, updating balances accordingly.
        """
        dealer_score = self._dealer.calculate_score()
        for player in self._players:
            player_score = player.calculate_score()
            result = ""
            if player_score > 21:
                print(f"{player.name} 🔥 busts! Loses 💸 {player._bet}.")
                player.adjust_balance(-player._bet)
                result = "lose"
            elif dealer_score > 21 or player_score > dealer_score:
                print(f"{player.name} 🏆 wins! Gains 💵 {player._bet}.")
                player.adjust_balance(player._bet)
                result = "win"
            elif player_score == dealer_score:
                print(f"{player.name} 🤝 ties with the dealer. Returns 💰 {player._bet}.")
                result = "tie"
            else:
                print(f"{player.name} ❌ loses to the dealer. Loses 💸 {player._bet}.")
                player.adjust_balance(-player._bet)
                result = "lose"

            # Adding the bet and result to the history for the current round
            player._add_history(player._bet, result)

    def _reset_game(self) -> None:
        """
        Resets the game state for the next round by reinitializing the deck and clearing hands and bets.
        """
        self._deck = Deck()
        for player in self._players + [self._dealer]:
            player._hand = []
            player._bet = 0
        self._current_round += 1

    def play(self) -> None:
        """
        Starts the game loop, playing the specified number of rounds and displaying final balances.
        """
        while self._current_round < self._rounds:
            self._play_round()
            self._reset_game()

        print("\n💰 Final Balances 💰")
        for player in self._players:
            print(f"{player.name} final balance: 💵 {player._balance}")
