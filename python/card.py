class Card():
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def describe(self):
        print('{} of {}'.format(self.face, self.suit))
