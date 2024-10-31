import pytest

from project.blackjack_game.src.card import Card
from project.blackjack_game.src.deck import Deck
from project.blackjack_game.src.player import Player, Dealer, Bot
from project.blackjack_game.src.game import Game


@pytest.fixture
def game_setup():
    game = Game(num_bots=3, rounds=1)
    return game


def test_initial_balance(game_setup):
    for player in game_setup.players:
        assert player.balance == 200


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
    assert len(deck.cards) == 51  # После одной карты в колоде должно остаться 51 карта


@pytest.mark.parametrize(
    "cards, expected_score",
    [
        (["10 ♥️", "9 ♦️", "3 ♠️"], 22),  # Игрок должен сброситься
        (["10 ♥️", "8 ♦️", "2 ♠️"], 20),  # Игрок не должен сброситься
    ],
)
def test_player_busts(cards, expected_score, game_setup):
    player = game_setup.players[0]
    for card_str in cards:
        rank, suit = card_str.split()
        player.add_card(Card(rank, suit))
    assert player.calculate_score() == expected_score


@pytest.mark.parametrize(
    "bet_amount, expected_balance",
    [
        (50, 150),  # допустимая ставка
        (300, 200),  # превышение баланса
    ],
)
def test_betting(game_setup, bet_amount, expected_balance):
    if bet_amount > 200:
        with pytest.raises(ValueError):
            game_setup.players[0].set_bet(bet_amount)
    else:
        game_setup.players[0].set_bet(bet_amount)
        game_setup.players[0].adjust_balance(-bet_amount)  # Уменьшаем баланс на ставку
        assert (
            game_setup.players[0].balance == expected_balance
        )  # Проверка баланса после установки ставки


def test_winner_determination(game_setup):
    # Устанавливаем ставки
    game_setup.players[0].set_bet(50)  # Первый игрок ставит 50
    game_setup.players[1].set_bet(100)  # Второй игрок ставит 100
    game_setup.players[2].set_bet(150)  # Третий игрок ставит 150

    # Добавляем карты игрокам
    game_setup.players[0].add_card(Card("10", "♥️"))  # Счет 10
    game_setup.players[0].add_card(Card("4", "♦️"))  # Счет 14

    game_setup.players[1].add_card(Card("Q", "♠️"))  # Счет 10
    game_setup.players[1].add_card(Card("7", "♣️"))  # Счет 17

    game_setup.players[2].add_card(Card("K", "♦️"))  # Счет 10
    game_setup.players[2].add_card(Card("5", "♥️"))  # Счет 15

    game_setup.dealer.add_card(Card("9", "♣️"))  # Счет 9
    game_setup.dealer.add_card(Card("6", "♠️"))  # Счет 15

    # Определяем победителя
    game_setup.determine_winner()

    # Проверяем балансы после определения победителя
    assert game_setup.players[0].balance == 150  # Первый игрок проиграл 50
    assert game_setup.players[1].balance == 300  # Второй игрок выиграл 100
    assert game_setup.players[2].balance == 200  # Третий игрок в ничью 150
