from .card import Card

class Deck():
    SUITS = ['spades', 'clubs', 'diamonds', 'hearts']
    FACES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']

    def __init__(self):
        self.cards = self.__create_deck()

    def __create_deck(self):
        cards = []
        for face in self.FACES:
            for suit in self.SUITS:
                cards.append(Card(face, suit))
        return cards

    def shuffle(self):
        return self

    def describe(self):
        for card in self.cards:
            card.describe()
