#print(len('ГришинаКсения')%2+1); # -> 2.blackjack 
from bot_player import ConservativeBot, AggressiveBot, RandomBot
from game import BlackjackGame

if __name__ == "__main__":
    bots = [
        ConservativeBot("ConservativeBot"),
        AggressiveBot("AggressiveBot"),
        RandomBot("RandomBot")
    ]
    game = BlackjackGame(bots)
    game.play_game()
