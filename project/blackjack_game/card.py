class Card:
    def __init__(self, rank: str, suit: str) -> None:
        """
        Initializes a card object.

        :param rank: The rank of the card (e.g., "A", "K", "4", "7").
        :param suit: The suit of the card (e.g., "♠️", "♥️", "♦️", "♣️").
        """
        self.rank = rank
        self.suit = suit

    def __str__(self) -> str:
        """
        Returns a string representation of the card in the format "Rank Suit".

        :return: A string representing the card.
        """
        return f"{self.rank} {self.suit}"

    def value(self) -> int:
        """
        Returns the numeric value of the card for the game.

        :return: The value of the card (11 for Ace, 10 for Jack, Queen, and King, otherwise the rank as an integer).
        """
        if self.rank in ["J", "Q", "K"]:
            return 10
        elif self.rank == "A":
            return 11
        else:
            return int(self.rank)
