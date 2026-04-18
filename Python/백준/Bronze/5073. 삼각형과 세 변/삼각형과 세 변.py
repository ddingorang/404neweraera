side = []
result = []
while 1 :
    a, b, c = map(int, input("").split())
    side.append(a)
    side.append(b)
    side.append(c)
    if (a, b, c) == (0, 0, 0) : break

    if max(side) >= sum(side) - max(side) : result.append('Invalid')
    else :
        if len(set(side)) == 1 : result.append('Equilateral')
        elif len(set(side)) == 2 : result.append('Isosceles')
        else : result.append('Scalene')

    side.clear()

for element in result :
    print(element)