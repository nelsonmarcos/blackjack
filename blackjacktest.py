import unittest
from blackjack import Blackjack

class BlackJackTest(unittest.TestCase):

    def test_start_game_function_return_initial_state(self):
        game = Blackjack()
        self.assertEquals(game.get_current_state(), ("start", "[1] Deal \n [2] Exit"))

    # def test_validate_player_input_to_start_a_game(self):
    #     game = Blackjack()
    #     game.evaluate_input(1)
    #     self.assertEqual()