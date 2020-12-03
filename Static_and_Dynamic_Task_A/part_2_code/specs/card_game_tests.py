import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card(clubs, 7)
        self.card2 = Card(spades, 5)
        self.card3 = Card(diamonds, 3)
        self.card4 = Card(hearts, 1)


@unittest.skip("Delete this line to run the test")
    def test_card_has_suit():
        pass


@unittest.skip("Delete this line to run the test")
    def card_has_value():
        pass


@unittest.skip("Delete this line to run the test")
    def test_check_for_ace():
        pass

@unittest.skip("Delete this line to run the test")
    def test_highest_card():
        pass


@unittest.skip("Delete this line to run the test")
    def test_cards_total():
        pass
