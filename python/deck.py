from .card import Card
import random

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
        shuffled_deck = []
        while self.cards:
            cards_left = len(self.cards)
            randomIndex = random.randint(0, cards_left-1) if cards_left > 1 else 0
            shuffled_deck.append(self.cards[randomIndex])
            del self.cards[randomIndex]
        self.cards = shuffled_deck
        return self

    def describe(self):
        for card in self.cards:
            card.describe()
