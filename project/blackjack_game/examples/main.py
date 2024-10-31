from project.blackjack_game.src.game import Game

# if there are import by ".module" and not "module" it doesnt find the files but testscript does
# though, if in src files import without ".", then the tests dont find files, but main does.
# ???


def main() -> None:
    """
    Main entry point for the Blackjack game.

    Initializes and starts the game with a specified number of bots and rounds.
    """
    game = Game(num_bots=3, rounds=5)
    game.play()


if __name__ == "__main__":
    main()
