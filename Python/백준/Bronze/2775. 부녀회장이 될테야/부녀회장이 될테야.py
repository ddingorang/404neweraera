testnum = int(input(""))
l = [[0]*15 for i in range(15)]
res = [0] * testnum

for a in range(15) :
    for b in range(1, 15) :
        if b == 1 : 
            l[a][b] = 1
            continue
        if a == 0 : 
            l[a][b] = b
            continue
        l[a][b] = l[a-1][b] + l[a][b-1]

for i in range(testnum) :
    k = int(input(""))
    n = int(input(""))
    res[i] = l[k][n]

for element in res :
    print(element)