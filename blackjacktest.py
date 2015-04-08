
import unittest
from blackjack import Blackjack, Card, Deck, Player, Dealer, get_hand_total, show_winner


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



class DeckTest(unittest.TestCase):
    def testDrawCard(self):
        deck = Deck()
        self.assertEqual(48, deck.get_size())
        card = deck.get_card()
        self.assertEqual(47, deck.get_size())
        self.assertFalse(deck.card_in_deck(card))

    def testDeckSize(self):
        deck = Deck()
        self.assertEqual(48, deck.get_size())

    def testCardInDeck(self):
        card = Card('S', 'T')
        deck = Deck()
        self.assertTrue(deck.card_in_deck(card))

    def testCardValue(self):
        card = Card('C', 'K')
        self.assertEqual(10, card.get_value())
        card = Card('C', '5')
        self.assertEqual(5, card.get_value())

    def testHandTotal(self):
        hand = [Card('C', '2'), Card('C', '6'), Card('C', '8'), Card('C', 'K')]
        self.assertEqual(26, get_hand_total(hand))

    def testWinnerPlayerMoreThan21(self):
        player = [Card('C', '2'), Card('C', '6'), Card('C', '8'), Card('C', 'K')]
        dealer = [Card('S', 'Q'), Card('S', '8')]
        self.assertEqual("dealer", show_winner(dealer, player))

    def testWinnerDealerMoreThan21(self):
        player = [Card('C', '2'), Card('C', '6'), Card('C', 'K')]
        dealer = [Card('S', 'Q'), Card('S', '8'), Card('H', '5')]
        self.assertEqual("player", show_winner(dealer, player))

    def testWinnerPlayer(self):
        player = [Card('C', '2'), Card('C', '6'), Card('C', 'K')]
        dealer = [Card('S', 'Q'), Card('H', '5')]
        self.assertEqual("player", show_winner(dealer, player))

    def testWinnerDealer(self):
        player = [Card('C', '2'), Card('C', '6'), Card('C', 'K')]
        dealer = [Card('S', 'Q'), Card('H', '9')]
        self.assertEqual("dealer", show_winner(dealer, player))

    def testWinnerSameTotal(self):
        player = [Card('C', '2'), Card('C', '6')]
        dealer = [Card('S', '3'), Card('H', '5')]
        self.assertEqual("dealer", show_winner(dealer, player))
