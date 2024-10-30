from .game import Game

if __name__ == "__main__":
    game = Game(num_bots=3, rounds=5)
    game.play()
