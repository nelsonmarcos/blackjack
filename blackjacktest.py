
import unittest
from blackjack import Blackjack, Card, Deck, Player, Dealer


class BlackJackTest(unittest.TestCase):

    def setUp(self):
        self.game = Blackjack()

    def test_start_game_with_default_options(self):
        self.assertEquals(self.game.options, "\n[1] Hit\n[2] Stand\n")

    def test_start_game_initialize_a_deck(self):
        self.assertIsInstance(self.game.deck, Deck)

    def test_start_game_initialize_a_player_and_a_dealer(self):
        self.assertIsInstance(self.game.player, Player)
        self.assertIsInstance(self.game.dealer, Dealer)

    # def test_start_game_initialize_a_player(self):
    #     self.assertIsInstance(self.game.deck, Player)


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
