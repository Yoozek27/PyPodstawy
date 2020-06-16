import math

inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]

if len(inputdata) == len(factortable):
    for i in range(len(inputdata)):
        minvalue = inputdata[i]-factortable[i]*inputdata[i]
        maxvalue = inputdata[i]+factortable[i]*inputdata[i]
        print('i =', i)
        print('minvalue =', minvalue)
        print('maxvalue =', maxvalue)
        mininteger = math.floor(minvalue)
        maxinteger = math.ceil(maxvalue)
        print('inputdata =', inputdata[i])
        print('mininteger =', mininteger)
        print('maxinteger =', maxinteger)
        

else:
    print('inputdata and factortable need to have equal number of elements')
