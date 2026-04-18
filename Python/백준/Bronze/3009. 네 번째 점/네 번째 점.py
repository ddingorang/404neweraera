x = {}
y = {}
for _ in range(3) :
    a, b = map(int,input("").split())
    if a in x : x[a] += 1
    else : x[a] = 1
    if b in y : y[b] += 1
    else : y[b] = 1

for name, element in x.items() :
    if element == 1 : print(f'{name} ', end="")
for name, element in y.items() :
    if element == 1 : print(name)