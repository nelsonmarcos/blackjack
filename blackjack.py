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
    def get_card(self):
        return Card('C', '2')
