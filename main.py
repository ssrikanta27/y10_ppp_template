import random

turnIndex = 0
cards = ['3♦', '3♣', '3♥', '3♠', '4♦', '4♣', '4♥', '4♠', '5♦', '5♣', '5♥', '5♠', '6♦', '6♣', '6♥', '6♠', '7♦', '7♣', '7♥', '7♠', '8♦', '8♣', '8♥', '8♠', '9♦', '9♣', '9♥', '9♠', '10♦', '10♣', '10♥', '10♠', 'J♦', 'J♣', 'J♥', 'J♠', 'Q♦', 'Q♣', 'Q♥', 'Q♠', 'K♦', 'K♣', 'K♥', 'K♠', 'A♦', 'A♣', 'A♥', 'A♠', '2♦', '2♣', '2♥', '2♠']
players = [[], [], [], []]
board = ['3♦']

def distributeCards(players, cards):
    list = cards
    while list != []:
        for num in range(4):
            players[num].append(random.choice(list))
            list.remove(players[num][-1])
    return players
# all cards distributed

def find3(players, turnIndex):
    if '3♦' in players[0]:
        turnIndex = 0
    elif '3♦' in players[1]:
        turnIndex = 1
    elif '3♦' in players[2]:
        turnIndex = 2
    elif '3♦' in players[3]:
        turnIndex = 3
    
    return turnIndex

# turnIndex is set
#start
def type1(turnIndex, players, board, cards):
    passcount = 0
    game = True
    
    while game:
        invalid = True
        print(f"It is player {turnIndex+1}'s turn")
        print(players[turnIndex])

        while invalid:

            cardIndex = input("Type in the position of the card: ")
            try:
                cardIndex = int(cardIndex)
                if cardIndex == 0:
                    invalid = False
                    passcount += 1
                else:
                    cardIndex -= 1
                    selectedCard = players[turnIndex][cardIndex]
                    if cards.index(selectedCard) >= cards.index(board[-1]):
                        board.append(selectedCard)
                        players[turnIndex].pop(cardIndex) #continue here
                        print(board[-1])
                        invalid = False
                    else:
                        print("INVALID")
            except:
                print("INVALID")
            
        if passcount == 4:
            return passcount
        else:
            turnIndex += 1
            if turnIndex > 3:
                turnIndex = 0
#end
                
def type2(turnIndex, players, board, cards):
    passcount = 0
    game = True
    cardIndex = []
    selectedCards = []
    value = 0
    while game:
        invalid = True
        print(f"It is player {turnIndex+1}'s turn")
        print(players[turnIndex])

        while invalid:

            cardIndexInput = input("Type in the position of the card: ")
            cardIndexInput2 = input("Type in the position of the card: ")
            try:
                cardIndex.append(int(cardIndexInput))
                cardIndex.append(int(cardIndexInput2))
                if cardIndex[0] == 0:
                    invalid = False
                    passcount += 1
                else:
                    cardIndex[0] -= 1
                    cardIndex[1] -= 1
                    selectedCards.append(players[turnIndex][cardIndex[0]])
                    selectedCards.append(players[turnIndex][cardIndex[1]])
                    if cards.index(selectedCards[0]) > cards.index(selectedCards[1]):
                        value = cards.index(selectedCards[0])
                        c1 = cards.index(selectedCards[1])
                        c2 = cards.index(selectedCards[0])
                    else:
                        value = cards.index(selectedCards[1])
                        c1 = cards.index(selectedCards[0])
                        c2 = cards.index(selectedCards[1])
                    if value > cards.index(board[-1]):
                        board.append(cards[c1])
                        board.append(cards[c2])
                        players[turnIndex].pop(cardIndex[0])
                        players[turnIndex].remove(cards) # fix this
                    
                        print(board[-2], board[-1])
                        invalid = False
                    else:
                        print("INVALID")
            except:
                print("INVALID")
            
            if passcount == 4:
                return passcount
            else:
                turnIndex += 1
                if turnIndex > 3:
                    turnIndex = 0 
            





play = True
players = distributeCards(players, cards)
print(players)
turnIndex = find3(players, turnIndex)
cards = ['3♦', '3♣', '3♥', '3♠', '4♦', '4♣', '4♥', '4♠', '5♦', '5♣', '5♥', '5♠', '6♦', '6♣', '6♥', '6♠', '7♦', '7♣', '7♥', '7♠', '8♦', '8♣', '8♥', '8♠', '9♦', '9♣', '9♥', '9♠', '10♦', '10♣', '10♥', '10♠', 'J♦', 'J♣', 'J♥', 'J♠', 'Q♦', 'Q♣', 'Q♥', 'Q♠', 'K♦', 'K♣', 'K♥', 'K♠', 'A♦', 'A♣', 'A♥', 'A♠', '2♦', '2♣', '2♥', '2♠']
while play:
    valid = False
    while not valid:
        gameType = input("Input a type of play, 1 - 5 excluding number 4: ")
        try:
            gameType = int(gameType)
            valid = True
        except:
            valid = False
    if gameType == 1:
        type1(turnIndex, players, board, cards)
    if gameType == 2:
        type2(turnIndex, players, board, cards)