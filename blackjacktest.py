import unittest
from blackjack import Blackjack, Card, Deck, SUITS, RANKS, get_hand_total, show_winner

class BlackJackTest(unittest.TestCase):
    def test_start_game_function_return_options(self):
        game = Blackjack()
#        self.assertEquals(game.current_state(), "[1] Deal \n [2] Exit")


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
