"""
Deal a hand of 5 cards
"""
import random

suits = ['♠︎', '♣︎', '♥︎', '♦︎']
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

cards = []
hand = []

for suit in suits:
    for value in values:
        cards.append(suit + value)

print(cards)

for i in range(5):
    choice = random.choice(cards)
    hand.append(choice)
    cards.remove(choice)
print(hand)
