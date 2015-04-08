import random
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


class Blackjack(object):
    def __init__(self):
        self.state = "start"
        self.states = {
            "start": "[1] Deal \n [2] Exit",
            "game": "dealer: %(dc1)s, %(dc2)s\nplayer: %(pc1)s, %(pc2)s, %(pc3)s\n\n[1] Hit\n[2] Stand\n[3] Double\n[4] Split"
        }

    def get_current_state(self):
        return self.state

class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

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




class Player(object):
    pass
