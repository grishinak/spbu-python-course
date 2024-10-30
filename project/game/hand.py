from card import Card


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card):
        self.cards.append(card)

    def calculate_score(self):
        score = sum(card.value() for card in self.cards)
        aces = sum(1 for card in self.cards if card.rank == "A")
        while score > 21 and aces:
            score -= 10
            aces -= 1
        return score

    def __repr__(self):
        return f"{self.cards} (Score: {self.calculate_score()})"
