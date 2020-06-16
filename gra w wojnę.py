import random

colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]
allCards = []
player1 = []
player2 = []

for i in colors:
    for j in figures:
        aCard = j.copy()
        aCard['Color'] = i
        allCards.append(aCard)
    print(allCards)

random.shuffle(allCards)
maxCards = len(allCards)

for i in range(0, maxCards):
    if i%2 == 0:
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])

print('allCards:', allCards)
print('player1:', player1)
print('player2:', player2)
count = 0

while len(player1) > 0 and len(player2) > 0:
    count += 1
    print('\nRound number:', count)
    card1 = player1[0]
    card2 = player2[0]

    print('Player 1 card:', card1['Figure'])
    print('Player 2 card:', card2['Figure'])
    if card1['Power'] > card2['Power']:
        print('Player 1 won the round')
        player1.pop(0)
        player2.pop(0)          
        player1.append(card1)
        player1.append(card2)
    elif card1['Power'] < card2['Power']:
        print('Player 2 won the round')
        player1.pop(0)
        player2.pop(0)  
        player2.append(card2)
        player2.append(card1)
    elif card1['Power'] == card2['Power']:
        cards1 = [card1]
        cards2 = [card2]
        warCount = 0
        while True:
            warCount += 1
            if warCount % 2 != 0:
                cards1.append(player1[warCount])
                cards2.append(player2[warCount])
                print('warCount:', warCount)
            elif warCount % 2 == 0:
                cards1.append(player1[warCount])
                cards2.append(player2[warCount])
                print('Player 1 card:', cards1[warCount]['Figure'])
                print('Player 2 card:', cards2[warCount]['Figure'])
                if cards1[warCount]['Power'] > cards2[warCount]['Power']:
                    print('Player 1 won the round')
                    for i in range(warCount):
                        player1.pop(i)
                        player2.pop(i)
                    player1.append(cards1)
                    player1.append(cards2) 
                    break
                elif cards1[warCount]['Power'] < cards2[warCount]['Power']:
                    print('Player 2 won the round')
                    for i in range(warCount):
                        player1.pop(i)
                        player2.pop(i)
                    player2.append(cards2)
                    player2.append(cards1)                         
                    break
                elif cards1[warCount]['Power'] == cards2[warCount]['Power']:
                    continue
                       
    print(len(player1), len(player2))
else:
    if len(player2) == 0:
        print('\nPlayer 1 won the game!')
    elif len(player1) == 0:
        print('\nPlayer 2 won the game!')
    

