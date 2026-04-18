angles = []
for _ in range(3) :
    n = int(input(""))
    angles.append(n)

if sum(angles) != 180 : print('Error')
else :
    if set(angles) == {60} : print('Equilateral')
    elif len(set(angles)) == 2 : print('Isosceles')
    else : print('Scalene')