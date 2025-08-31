# Single Player UNO Game
import random

colors = ['Red', 'Green', 'Blue', 'Yellow']
values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Skip', 'Reverse', 'Draw Two']
wildCards = ['Wild', 'Wild Draw Four']

players = []
colors = ['Red', 'Green', 'Blue', 'Yellow']
values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Skip', 'Reverse', 'Draw Two']
wildCards = ['Wild', 'Wild Draw Four']

def createDeck():
    deck = []
    for color in colors:
        for value in values:
            deck.append((color, value))
            if value != '0':
                deck.append((color, value)) 
    for wild in wildCards:
        for _ in range(4):
            deck.append(('Black', wild))
    random.shuffle(deck)
    return deck