from project.blackjack_game.src.game import Game


def main() -> None:
    """
    Main entry point for the Blackjack game.

    Initializes and starts the game with a specified number of bots and rounds.
    """
    game = Game(num_bots=3, rounds=5)
    game.play()


if __name__ == "__main__":
    main()
