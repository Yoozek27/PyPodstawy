import random

def dice():
    dices = []
   
    for i in range(5):
        dices.append(random.randint(1, 6))

    dices.sort()
    print(dices)
while True:
    input('\nPress enter to throw dices')
    dice()
