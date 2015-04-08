import random

class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

class Deck(object):
    SUITS = ('C', 'S', 'H', 'D')
    RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
    VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

        random.shuffle(self.cards)

    def get_card(self):
        return Card('C', '2')

    def get_size(self):
        return len(self.cards)

class Player(object):
    pass