import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.cards = []
        self.card1 = Card("clubs", 7)
        self.cards.append(self.card1)
        self.card2 = Card("spades", 5)
        self.cards.append(self.card2)
        self.card3 = Card("diamonds", 3)
        self.cards.append(self.card3)
        self.card4 = Card("hearts", 1)
        self.cards.append(self.card4)
        self.card_game = CardGame() 

# @unittest.skip("Delete this line to run the test")
    def test_check_for_ace_is_ace(self):

        self.assertEqual(1, self.card_game.check_for_ace(self.card4))

# @unittest.skip("Delete this line to run the test")
    def test_check_for_ace_not_ace(self):

        self.assertEqual(1, self.card_game.check_for_ace(self.card3))

#    @unittest.skip("Delete this line to run the test")
    def test_highest_card(self):
        self.assertEqual(7, self.card_game.highest_card(self.card1, self.card2))

#    @unittest.skip("Delete this line to run the test")
    def test_cards_total(self):
        self.assertEqual(13, self.card_game.cards_total(self.cards))