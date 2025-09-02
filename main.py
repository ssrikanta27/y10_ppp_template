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

# Gameplay Functions
def getNextPlayer():
    global currentPlayer, playDirection, players # The global variables allow the variables to be accessed anywhere in the code.
    currentPlayer = (currentPlayer + playDirection) % len(players) # The percentage sign is a modulus it is a good way to loop without using if

def isPlayable(card, topCard):
    return (card[0] == topCard[0] or card[1] == topCard[1] or card[0] == 'Black') #checking if the card is wild, or if colour is the same or if the number is the same
# If any of the statements are true it will output true else it will output false
def drawCard(playerIndex):
    if not drawPile: # Checks if list is empty
        reshuffleDiscardIntoDraw() #dfining this later
    card = drawPile.pop()
    hands[playerIndex].append(card)
    return card