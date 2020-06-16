import sys

##order_of_succession = ['Deak', 'Windy', 'Luke', 'Biggs']
order_of_succession = sys.argv
order_of_succession.pop(0)

for i, item in enumerate(order_of_succession, start=1):
    print(i, ". ", item, sep='')
