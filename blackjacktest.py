import unittest
from blackjack import Blackjack

class BlackJackTest(unittest.TestCase):
    def test_start_game_function_return_options(self):
        game = Blackjack()
        self.assertEquals(game.current_state(), "[1] Deal \n [2] Exit")
