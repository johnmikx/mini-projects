import random

cards = []
suits = ['spades', 'clubs', 'hearts', 'diamonds']
ranks = [
    {'rank': 'A', 'value': 11},
    {'rank': '2', 'value': 2},
    {'rank': '3', 'value': 3},
    {'rank': '4', 'value': 4},
    {'rank': '5', 'value': 5},
    {'rank': '6', 'value': 6},
    {'rank': '7', 'value': 7},
    {'rank': '8', 'value': 8},
    {'rank': '9', 'value': 9},
    {'rank': '10', 'value': 10},
    {'rank': 'J', 'value': 10},
    {'rank': 'Q', 'value': 10},
    {'rank': 'K', 'value': 10}
]

for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])

def shuffle():
    random.shuffle(cards)

def deal(number):
    cards_dealt = []
    for x in range(number):
        card = cards.pop()
        cards_dealt.append(card)
    return cards_dealt

shuffle()
card = deal(1)[0]
print(card[1]['value'])