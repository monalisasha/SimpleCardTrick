# Created by Monalisa Sha on 09-07-2019

import random
from random import shuffle

# Deck of 52 cards
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suites = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
deck = [v for s in suites for v in values]

#For drawing random 10 cards
def draw_card(n, deck):
    random.shuffle(deck)
    cards_selected = [deck.pop() for k in range(n)]
    print(cards_selected)
    for i in range(0, 5):
        cards_selected += [cards_selected.pop(0)]
    print(cards_selected)

    left = cards_selected[:5]
    right = cards_selected[5:]

    new_deck = right + left
    print(new_deck)

    for i in range(0, 6):
        new_deck += [new_deck.pop(0)]

    print([new_deck[3]])
