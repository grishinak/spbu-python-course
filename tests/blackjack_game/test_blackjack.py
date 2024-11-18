import pytest

from project.blackjack_game.src.card import Card
from project.blackjack_game.src.deck import Deck
from project.blackjack_game.src.game import Game


@pytest.fixture
def game_setup():
    game = Game(num_bots=3, rounds=1)
    return game


def test_initial_balance(game_setup):
    for player in game_setup._players:
        assert player._balance == 200


@pytest.mark.parametrize(
    "rank, suit, expected_value",
    [
        ("A", "♥️", 11),
        ("10", "♦️", 10),
        ("K", "♣️", 10),
    ],
)
def test_card_value(rank, suit, expected_value):
    card = Card(rank, suit)
    assert card.value() == expected_value


def test_deck_draw(game_setup):
    deck = Deck()
    first_card = deck.draw()
    assert first_card is not None
    assert (
        len(deck._cards) == 51
    )  # After one card, there should be 51 cards left in the deck


@pytest.mark.parametrize(
    "cards, expected_score",
    [
        (["10 ♥️", "9 ♦️", "3 ♠️"], 22),  # The player must bust
        (["10 ♥️", "8 ♦️", "2 ♠️"], 20),  # The player must not bust
    ],
)
def test_player_busts(cards, expected_score, game_setup):
    player = game_setup._players[0]
    for card_str in cards:
        rank, suit = card_str.split()
        player.add_card(Card(rank, suit))
    assert player.calculate_score() == expected_score


@pytest.mark.parametrize(
    "bet_amount, expected_balance",
    [
        (50, 150),  # acceptable bet
        (
            300,
            200,
        ),  # exceeding the balance (no bet) (in bot game its impossible, checking the func)
    ],
)
def test_betting(game_setup, bet_amount, expected_balance):
    if bet_amount > 200:
        with pytest.raises(ValueError):
            game_setup._players[0].set_bet(bet_amount)
    else:
        game_setup._players[0].set_bet(bet_amount)
        game_setup._players[0].adjust_balance(
            -bet_amount
        )  # Reducing the balance by a bet
        assert (
            game_setup._players[0]._balance == expected_balance
        )  # Checking the balance after setting the bet


def test_winner_determination(game_setup):
    # Setting the bets
    game_setup._players[0].set_bet(50)  # The first player bets 50
    game_setup._players[1].set_bet(100)  # The second player bets  100
    game_setup._players[2].set_bet(150)  # The third player bets 150

    game_setup._players[0].add_card(Card("10", "♥️"))  # score 10
    game_setup._players[0].add_card(Card("4", "♦️"))  # score 14

    game_setup._players[1].add_card(Card("Q", "♠️"))  # score 10
    game_setup._players[1].add_card(Card("7", "♣️"))  # score 17

    game_setup._players[2].add_card(Card("K", "♦️"))  # score 10
    game_setup._players[2].add_card(Card("5", "♥️"))  # score 15

    game_setup._dealer.add_card(Card("9", "♣️"))  # score 9
    game_setup._dealer.add_card(Card("6", "♠️"))  # score 15

    game_setup._determine_winner()

    assert game_setup._players[0]._balance == 150  # player lost 50
    assert game_setup._players[1]._balance == 300  #  player win 100
    assert (
        game_setup._players[2]._balance == 200
    )  #  player ties with bet of 150 - balance stays 200
