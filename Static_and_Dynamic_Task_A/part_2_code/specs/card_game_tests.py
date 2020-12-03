import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("clubs", 7)
        self.card2 = Card("spades", 5)
        self.card3 = Card("diamonds", 3)
        self.card4 = Card("hearts", 1)


# @unittest.skip("Delete this line to run the test")
    def test_card_has_suit(self):
        self.assertEqual("clubs", self.card1.suit)

# @unittest.skip("Delete this line to run the test")
    def card_has_value(self):
        self.assertEqual(7, self.card1.value)

# @unittest.skip("Delete this line to run the test")
    def test_check_for_ace(self):
        self.card_game = CardGame(self.card3, self.card4) 
        self.assertEqual(1, self.card_game.check_for_ace(self.card1, self.card2))

    @unittest.skip("Delete this line to run the test")
    def test_highest_card(self):
        self.card_game = CardGame(self.card1, self.card2) 
        self.assertEqual(7, self.card_game.highest_card(self.card1, self.card2))

    @unittest.skip("Delete this line to run the test")
    def test_cards_total(self):
        self.card_game = CardGame(self.card1, self.card2) 
        self.assertEqual(13, self.card_game.cards_total(self.card1, self.card2))