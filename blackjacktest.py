import unittest
from blackjack import Blackjack, Card, Deck, SUITS, RANKS

class BlackJackTest(unittest.TestCase):

    def test_start_game_function_return_initial_state(self):
        game = Blackjack()
        self.assertEquals(game.get_current_state(), ("start", "[1] Deal \n [2] Exit"))

    # def test_validate_player_input_to_start_a_game(self):
    #     game = Blackjack()
    #     game.evaluate_input(1)
    #     self.assertEqual()


class DeckTest(unittest.TestCase):
    def testDrawCard(self):
        deck = Deck()
        self.assertEqual(52, deck.get_size())
        card = deck.get_card()
        self.assertEqual(51, deck.get_size())
        self.assertFalse(deck.card_in_deck(card))

    def testDeckSize(self):
        deck = Deck()
        self.assertEqual(52, deck.get_size())

    def testCardInDeck(self):
        card = Card('S', 'T')
        deck = Deck()
        self.assertTrue(deck.card_in_deck(card))
