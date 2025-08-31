import random

# Set Up
colors = ['Red', 'Green', 'Blue', 'Yellow']
values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Skip', 'Reverse', 'Draw Two']
wildCards = ['Wild', 'Wild Draw Four']

players = []
hands = []
discardPile = []
drawPile = []
currentPlayer = 0
playDirection = 1

# Setup Functions
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

def dealCards(deck, numPlayers):
    playerHands = [[] for _ in range(numPlayers)] # Basically if 2 people play this would make [[], []]
    for _ in range(7):
        for i in range(numPlayers):
            playerHands[i].append(deck.pop())
    return playerHands

def initializeGame(numPlayers):
    global players, hands, drawPile, discardPile, currentPlayer, playDirection # You Could pass these as parameters but the code is slightly easier to read this way
    players = ['You'] + [f'Bot {i}' for i in range(1, numPlayers)] # Sets the different player (Not their cards)
    drawPile = createDeck()
    hands = dealCards(drawPile, numPlayers) # Sets their cards
    discardPile.append(drawPile.pop()) 
    currentPlayer = 0
    playDirection = 1
