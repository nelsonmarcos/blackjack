
import random

SUITS = ('C', 'S', 'H', 'D')
#RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


class Blackjack(object):

    def __init__(self):
        self.options = "\n[1] Hit\n[2] Stand\n"
        self.deck = Deck()
        self.player = [self.deck.get_card(), self.deck.get_card()]
        self.dealer = [self.deck.get_card(), self.deck.get_card()]

    def evaluate_player_input(self, i):
        if i == "1":
            self.player.append(self.deck.get_card())
            self.current_game_state()
        else:
            print "Winner: %s" % show_winner(self.dealer, self.player)

    def print_hand(self, hand):
        hand_str = ''
        for card in hand:
            hand_str += str(card) + ','
        return hand_str

    def start(self):
        self.current_game_state()

    def current_game_state(self):
        print "dealer: %s\nplayer: %s\n%s" % (self.print_hand(self.dealer),
                                              self.print_hand(self.player),
                                              self.options)
        playerInput = raw_input()
        self.evaluate_player_input(playerInput)


class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_value(self):
        return VALUES[self.rank]

    def get_str_card(self):
        return self.suit + self.rank

    def __str__(self):
        return self.get_str_card()


class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

        random.shuffle(self.cards)

    def get_card(self):
        card = self.cards[0]
        self.cards = self.cards[1:len(self.cards)]
        return card

    def get_size(self):
        return len(self.cards)

    def card_in_deck(self, card):
        for carddeck in self.cards:
            if card.rank == carddeck.rank and card.suit == carddeck.suit:
                return True
        return False


def get_hand_total(hand):
    total = 0
    for card in hand:
        total += card.get_value()
    return total


def show_winner(dealer_hand, player_hand):
    dealer_total = get_hand_total(dealer_hand)
    player_total = get_hand_total(player_hand)
    if player_total > 21:
        return "dealer"
    elif dealer_total > 21:
        return "player"
    elif player_total > dealer_total:
        return "player"
    else:
        return "dealer"


if __name__ == "__main__":
    game = Blackjack()
    game.start()
