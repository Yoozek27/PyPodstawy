import random

def dice():
    num = random.randint(1, 6)

    if num == 1:
        print('''
    
      o 
       
    ''') 
    if num == 2:
        print('''
        o
    
    o   
    ''')
    if num == 3:
        print('''
        o
      o 
    o
    ''')
    if num == 4:
        print('''
    o   o
     
    o   o   
    ''')
    if num == 5:
        print('''
    o   o
      o
    o   o   
    ''')
    if num == 6:
        print('''
    o   o
    o   o
    o   o  
    ''')
        
while True:
    input()
    dice()
