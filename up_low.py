def myfunc(a):
    b = ''
    for i in range(len(a)):
        if i%2 ==0:
           b += a[i].upper()
        else:
           b += a[i].lower()
    print(b)

myfunc('abcdef')
