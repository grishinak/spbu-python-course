from card import Deck
from bot_player import BotPlayer

class BlackjackGame:
    def __init__(self, bots, max_steps=10):
        self.deck = Deck()
        self.bots = bots
        self.max_steps = max_steps
        self.current_step = 0

    def show_state(self):
        print(f"Step: {self.current_step}")
        for bot in self.bots:
            print(f"{bot.name}: {bot.hand}")

    def play_round(self):
        self.current_step += 1
        print(f"\nRound {self.current_step}")
        for bot in self.bots:
            bot.reset_hand()
            bot.hand.add_card(self.deck.draw_card())
            bot.hand.add_card(self.deck.draw_card())
            bot.take_turn(self.deck)
        self.show_state()

    def check_winner(self):
        winners = [bot for bot in self.bots if bot.hand.calculate_score() <= 21]
        if winners:
            max_score = max(bot.hand.calculate_score() for bot in winners)
            return [bot for bot in winners if bot.hand.calculate_score() == max_score]
        return []

    def play_game(self):
        while self.current_step < self.max_steps:
            self.play_round()
            winners = self.check_winner()
            if winners:
                print("\nWinners:")
                for bot in winners:
                    print(f"{bot.name} with score: {bot.hand.calculate_score()}")
                return
        print("\nNo winners within max steps")
