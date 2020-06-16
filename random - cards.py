import random

colors = ['Hearts','Diamonds','Clubs','Spades']
figures = ['Ace','King','Queen','Jack','10','9']
allCards = []
player1 = []
player2 = []

for i in colors:
    for j in figures:
        allCards.append(j + ' - ' + i)

random.shuffle(allCards)
maxCards = len(allCards)

for i in range(0, maxCards - 1):
    if i%2 == 0:
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])

print('allCards:', allCards)
print('player1:', player1)
print('player2:', player2)
