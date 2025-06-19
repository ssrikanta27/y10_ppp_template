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

                
def type2(turnIndex, players, board, cards):
    passes = 0
    game = True
    while game:
        valid = False
        while not valid:
            print(f"Player{turnIndex+1}'s turn")
            print(players[turnIndex])
            cardIndex = []
            selectedCards = []
            cardChoice1 = input("Enter the position of the first card: ")
            try:
                if int(cardChoice1) == 0:
                    passes += 1
                    turnIndex += 1
                    if turnIndex > 3:
                        turnIndex = 0
                    if passes == 4:
                        return passes
                else:           
                    cardChoice2 = input("Enter the position of the second card: ")
                    try:
                        # Validate and add into the cardIndex list
                        cardIndex.append(int(cardChoice1)-1)
                        cardIndex.append(int(cardChoice2)-1)
                        # Get the string of the card
                        selectedCards.append(players[turnIndex][cardIndex[0]])
                        selectedCards.append(players[turnIndex][cardIndex[1]])
                        # Compare the index of the card 
                        # append the highest value card at the end of selectedCards
                        if cards.index(selectedCards[0]) > cards.index(selectedCards[1]):
                            high = selectedCards[0]
                            low = selectedCards[1]
                            selectedCards[0] = low
                            selectedCards[1] = high
                        else:
                            pass
                        # Compare the highest value card the previous card in the board
                        # If the value is larger then append both values to the board
                        if cards.index(selectedCards[1]) > cards.index(board[-1]):
                            for i in range(2):
                                board.append(selectedCards[i])
                                valid == True
                            print(board[-2])
                            print(board[-1])
                            turnIndex += 1
                            if turnIndex > 3:
                                turnIndex = 0
                            
                        else:
                            valid == False
                            print("INVALID")
                    except:
                        print("INVALID")

            except:
                print("INVALID")


def type3(turnIndex, players, board, cards):
    cardChoices = []
    cardValues = [-1]
    cardChoiceIndex1 = int(input("Input the position of the 1st card: ")) - 1
    cardChoiceIndex2 = int(input("Input the position of the 2nd card: ")) - 1
    cardChoiceIndex3 = int(input("Input the position of the 3d card: ")) - 1
    cardChoices.append(players[turnIndex][cardChoiceIndex1])
    cardChoices.append(players[turnIndex][cardChoiceIndex2])
    cardChoices.append(players[turnIndex][cardChoiceIndex3])
    players[turnIndex].pop(cardChoiceIndex1)
    players[turnIndex].pop(cardChoiceIndex2)
    players[turnIndex].pop(cardChoiceIndex3)
    for i in range(3):
        if cards.index(cardChoices[i]) > cardValues[-1]:
            pass



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