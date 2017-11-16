from python.deck import Deck

def deck_o_cards():
    return Deck().shuffle()

deck_o_cards().describe()
print('this deck has {} cards'.format(len(deck_o_cards().cards)))
