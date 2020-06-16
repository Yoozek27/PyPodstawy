import random

lista = []

for i in range(10):
    lista.append(random.randint(1,100))

print('Losowe 10 liczb z zakresu 1 do 100:', lista)



number1 = random.randint(1,100)
count = 0

while True:
    count += 1
    number2 = random.randint(1,100)
    print('Numer próby: %d \nPoszukiwana liczba: %d \nWylosowana liczba: %d \n' % (count, number1, number2))
    if number1 == number2:
        print('Udało się wylosować poszukiwaną liczbę w próbie numer', count)
        break
