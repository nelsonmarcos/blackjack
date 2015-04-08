SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

class Deck(object):
    def get_card(self):
        return Card('C', '2')

class Player(object):
    pass