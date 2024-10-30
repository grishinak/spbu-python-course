from card import Deck
from bot_player import BotPlayer, Dealer


class BlackjackGame:
    def __init__(self, bots, max_steps=10):
        self.deck = Deck()
        self.bots = bots
        self.dealer = Dealer()  # Добавляем дилера
        self.max_steps = max_steps
        self.current_step = 0

    def show_state(self):
        print(f"\n--- Step {self.current_step} ---")
        for bot in self.bots:
            print(f"{bot.name}: {bot.hand}")
        print(f"{self.dealer.name}: {self.dealer.hand}")

    def play_round(self):
        self.current_step += 1
        print(f"\nRound {self.current_step}")

        # Начальная раздача для всех ботов и дилера
        for bot in self.bots:
            bot.reset_hand()
            bot.hand.add_card(self.deck.draw_card())
            bot.hand.add_card(self.deck.draw_card())
            print(f"{bot.name} starts with: {bot.hand}")
        self.dealer.reset_hand()
        self.dealer.hand.add_card(self.deck.draw_card())
        self.dealer.hand.add_card(self.deck.draw_card())
        print(f"{self.dealer.name} starts with: {self.dealer.hand}")

        # Каждый бот выполняет ход
        for bot in self.bots:
            print(f"\n{bot.name} takes turn:")
            while True:
                current_score = bot.hand.calculate_score()
                if current_score >= 21:
                    print(f"{bot.name} stops (Score: {current_score})")
                    break
                print(f"Current hand for {bot.name}: {bot.hand}")
                bot.hand.add_card(self.deck.draw_card())
                print(f"New card added. {bot.name}'s hand: {bot.hand}")

        # Ход дилера
        print(f"\n{self.dealer.name} takes turn:")
        self.dealer.take_turn(self.deck)

    def check_winner(self):
        dealer_score = self.dealer.hand.calculate_score()
        if dealer_score > 21:
            dealer_score = 0  # Дилер проигрывает, если его очки больше 21

        winners = []
        for bot in self.bots:
            bot_score = bot.hand.calculate_score()
            if bot_score <= 21 and (bot_score > dealer_score or dealer_score > 21):
                winners.append(bot)
            elif bot_score == dealer_score:
                print(f"{bot.name} ties with {self.dealer.name} (Score: {bot_score})")

        if not winners and dealer_score <= 21:
            winners.append(self.dealer)
        return winners

    def play_game(self):
        while self.current_step < self.max_steps:
            self.play_round()
            self.show_state()
            winners = self.check_winner()
            if winners:
                print("\nWinners:")
                for winner in winners:
                    print(f"{winner.name} with score: {winner.hand.calculate_score()}")
                return
        print("\nNo winners within max steps")
