def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()
while True:
    a_str = input('Wpisz współczynnik a: ')
    if check_int(a_str) == False:
        print('Błąd. Wpisz liczbę całkowitą!')
        continue
    else:
        a = int(a_str)
        if a == 0:
            print('To nie jest równanie kwadratowe!')
            continue

    b_str = input('Wpisz współczynnik b: ')
    if check_int(b_str) == False:
        print('Błąd. Wpisz liczbę całkowitą!')
        continue
    else:
        b = int(b_str)

    c_str = input('Wpisz współczynnik c: ')
    if check_int(c_str) == False:
        print('Błąd. Wpisz liczbę całkowitą!')
        continue
    else:
        c = int(c_str)
    print('Wprowadzone równanie kwadratowe: %dx2 + %dx + %d' % (a, b, c))
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print('delta < 0, brak miejsc zerowych\ndelta = %f' % (delta))

    if delta == 0:
        x1 = (-b - delta ** 0.5) / (2*a)
        print('delta = 0, jedno miejsce zerowe\nx1 = %f' % (x1))

    if delta > 0:
        x1 = (-b - delta ** 0.5) / (2*a)
        x2 = (-b + delta ** 0.5) / (2*a)
        print('delta > 0, dwa miejsca zerowe\ndelta = %f, x1 = %f, x2 = %f' % (delta, x1, x2))
    print('\n')
    
