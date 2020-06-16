initialCapital = 20000
percent = 0.03
maxTimeYears = 10
years = 1
capital = initialCapital

while years <= maxTimeYears:
    interest = capital * percent
    capital += interest
    print('Capital after', years, 'years:', '%.2f' % capital,
          '\nInterest in year', years, 'is:', '%.2f' % interest, '\n')
    years += 1
else:
    print('Total interest is:', '%.2f' % (capital - initialCapital))
