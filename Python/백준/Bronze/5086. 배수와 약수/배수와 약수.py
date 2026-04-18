a = 0
b = 0
l = []
while 1 :
    a, b = map(int, input("").split())
    if a == 0 and b == 0 : break
    elif b // a >= 1 and b % a == 0 :
        l.append('factor')
    elif a // b >= 1 and a % b == 0 :
        l.append('multiple')
    else :
        l.append('neither')

for element in l :
    print(element)
