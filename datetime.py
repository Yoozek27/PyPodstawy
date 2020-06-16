import datetime

today = datetime.date.today()
print(today)


print('--------------------')


bornDateM = datetime.date(1996,12,20)
bornDateW = datetime.date(1994,3,9)
print(today - bornDateM)
print(today - bornDateW)
print(bornDateM - bornDateW)
print(datetime.date(2021,7,24) - bornDateW)
