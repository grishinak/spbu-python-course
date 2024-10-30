import random
from .deck import Deck
from .player import Bot, Dealer

class Game:
    def __init__(self, num_bots=3, rounds=5):
        self.deck = Deck()
        self.players = [Bot(f"Bot {i + 1}") for i in range(num_bots)]
        self.dealer = Dealer()
        self.rounds = rounds
        self.current_round = 0

    def set_bets(self):
        for player in self.players:
            bet = random.randint(1, min(100, player.balance))
            player.set_bet(bet)
            print(f"{player.name} bets 💰 {player.bet}")

    def deal_initial_cards(self):
        for player in self.players:
            player.hand = [self.deck.draw(), self.deck.draw()]
        self.dealer.hand = [self.deck.draw(), self.deck.draw()]

    def show_hands(self):
        for player in self.players:
            print(
                f"{player.name} 🃏 hand: {', '.join(map(str, player.hand))}, Score: {player.calculate_score()} 💰 Bet: {player.bet}, Balance: {player.balance}"
            )
        print(
            f"Dealer 🃏 hand: {', '.join(map(str, self.dealer.hand))}, Score: {self.dealer.calculate_score()}"
        )

    def play_round(self):
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

    def determine_winner(self):
        dealer_score = self.dealer.calculate_score()
        for player in self.players:
            player_score = player.calculate_score()
            if player_score > 21:
                print(f"{player.name} 🔥 busts! Loses 💸 {player.bet}.")
                player.adjust_balance(-player.bet)
            elif dealer_score > 21 or player_score > dealer_score:
                print(f"{player.name} 🏆 wins! Gains 💵 {player.bet}.")
                player.adjust_balance(player.bet)
            elif player_score == dealer_score:
                print(f"{player.name} 🤝 ties with the dealer. Returns 💰 {player.bet}.")
            else:
                print(f"{player.name} ❌ loses to the dealer. Loses 💸 {player.bet}.")
                player.adjust_balance(-player.bet)

    def reset_game(self):
        self.deck = Deck()
        for player in self.players + [self.dealer]:
            player.hand = []
            player.bet = 0
        self.current_round += 1

    def play(self):
        while self.current_round < self.rounds:
            self.play_round()
            self.reset_game()

        print("\n💰 Final Balances 💰")
        for player in self.players:
            print(f"{player.name} final balance: 💵 {player.balance}")
