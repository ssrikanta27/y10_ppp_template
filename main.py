import random

turnIndex = 0
cards = ['3♦', '3♣', '3♥', '3♠', '4♦', '4♣', '4♥', '4♠', '5♦', '5♣', '5♥', '5♠', '6♦', '6♣', '6♥', '6♠', '7♦', '7♣', '7♥', '7♠', '8♦', '8♣', '8♥', '8♠', '9♦', '9♣', '9♥', '9♠', '10♦', '10♣', '10♥', '10♠', 'J♦', 'J♣', 'J♥', 'J♠', 'Q♦', 'Q♣', 'Q♥', 'Q♠', 'K♦', 'K♣', 'K♥', 'K♠', 'A♦', 'A♣', 'A♥', 'A♠', '2♦', '2♣', '2♥', '2♠']
players = [[], [], [], []]
board = []

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
    
def type1(turnIndex, players, board):

    game = True
    while game:
        
        print(f"It is player {turnIndex+1}'s turn")
        print(players[turnIndex])

        cardIndex = int(input("Type in the position of the card: "))
        cardIndex -= 1
        selectedCard = players[turnIndex][cardIndex]
        board.append(selectedCard)
        players[turnIndex].pop(cardIndex) #continue here
        print(board[-1])

        turnIndex += 1
        if turnIndex > 3:
            turnIndex = 0
#end

    
players = distributeCards(players, cards)
print(players)
turnIndex = find3(players, turnIndex)
type1(turnIndex, players, board)