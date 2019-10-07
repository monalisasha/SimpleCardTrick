import random
from random import shuffle



values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
suites = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
deck = [[v + ' of ' + s,v] for s in suites for v in values]
print(deck)


def draw_card(n, deck):
    random.shuffle(deck)
    cards_selected = [deck.pop() for k in range(n)]

#     for i in range(n):
#         cards_selected += [cards_selected.pop(0)]
#
# left = cards_selected[:5]
#
# right = cards_selected[5:]
# new_deck = right + left
#
#
# for i in range(0,6):
#
#        cards_selected += [cards_selected.pop(0)]
#
# print (cards_selected[3])
