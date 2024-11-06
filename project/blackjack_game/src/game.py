import random
from .deck import Deck
from .player import (
    Bot,
    Dealer,
    AggressiveStrategy,
    ConservativeStrategy,
    RiskyStrategy,
    AdaptiveStrategy,
)
from typing import List


class Game:
    def __init__(self, num_bots: int = 3, rounds: int = 5) -> None:
        """
        Initializes a game of Blackjack with a specified number of bots and rounds.
        """
        self.deck = Deck()
        strategies = [
            AggressiveStrategy(),
            ConservativeStrategy(),
            RiskyStrategy(),
            AdaptiveStrategy(),
        ]

        self.players: List[Bot] = [
            Bot(f"Bot {i + 1}", strategy=strategies[i % len(strategies) + 1])
            for i in range(num_bots)
        ]

        self.dealer = Dealer()
        self.rounds = rounds
        self.current_round = 0

    def set_bets(self) -> None:
        """
        Sets bets for all players by randomly selecting a bet amount
        within the player's balance.
        """
        for player in self.players:
            bet = random.randint(1, min(100, player.balance))
            player.set_bet(bet)
            print(f"{player.name} bets 💰 {player.bet}")

    def deal_initial_cards(self) -> None:
        """
        Deals two initial cards to each player and the dealer.
        """
        for player in self.players:
            player.hand = [self.deck.draw(), self.deck.draw()]
        self.dealer.hand = [self.deck.draw(), self.deck.draw()]

    def show_hands(self) -> None:
        """
        Displays the hands and scores of all players and the dealer.
        """
        for player in self.players:
            print(
                f"{player.name} 🃏 hand: {', '.join(map(str, player.hand))}, "
                f"Score: {player.calculate_score()} 💰 Bet: {player.bet}, Balance: {player.balance}"
            )
        print(
            f"Dealer 🃏 hand: {', '.join(map(str, self.dealer.hand))}, "
            f"Score: {self.dealer.calculate_score()}"
        )

    def play_round(self) -> None:
        """
        Plays a single round of Blackjack, including setting bets, dealing cards,
        allowing players to make moves, and determining the winner.
        """
        print(f"\n🎲 Round {self.current_round + 1} 🎲")
        self.set_bets()
        self.deal_initial_cards()
        self.show_hands()

        for player in self.players:
            player.make_move(self.deck)
            print(f"{player.name} ends with score {player.calculate_score()}")

        while self.dealer.calculate_score() < 17:
            self.dealer.add_card(self.deck.draw())
        print(f"Dealer ends with score {self.dealer.calculate_score()}")

        self.determine_winner()

    def determine_winner(self) -> None:
        """
        Determines the winner of the round based on the scores of the players
        and the dealer, updating balances accordingly.
        """
        dealer_score = self.dealer.calculate_score()
        for player in self.players:
            player_score = player.calculate_score()
            result = ""
            if player_score > 21:
                print(f"{player.name} 🔥 busts! Loses 💸 {player.bet}.")
                player.adjust_balance(-player.bet)
                result = "lose"
            elif dealer_score > 21 or player_score > dealer_score:
                print(f"{player.name} 🏆 wins! Gains 💵 {player.bet}.")
                player.adjust_balance(player.bet)
                result = "win"
            elif player_score == dealer_score:
                print(f"{player.name} 🤝 ties with the dealer. Returns 💰 {player.bet}.")
                result = "tie"
            else:
                print(f"{player.name} ❌ loses to the dealer. Loses 💸 {player.bet}.")
                player.adjust_balance(-player.bet)
                result = "lose"

            # Adding the bet and result to the history for the current round
            player.add_history(player.bet, result)

    def reset_game(self) -> None:
        """
        Resets the game state for the next round by reinitializing the deck and clearing hands and bets.
        """
        self.deck = Deck()
        for player in self.players + [self.dealer]:
            player.hand = []
            player.bet = 0
        self.current_round += 1

    def play(self) -> None:
        """
        Starts the game loop, playing the specified number of rounds and displaying final balances.
        """
        while self.current_round < self.rounds:
            self.play_round()
            self.reset_game()

        print("\n💰 Final Balances 💰")
        for player in self.players:
            print(f"{player.name} final balance: 💵 {player.balance}")
