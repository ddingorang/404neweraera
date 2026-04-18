n = int(input())
l = []
count = []

def eratosthenes(limit) :
    primelist = [True] * (limit+1)
    p = 2
    while p*p <= limit:
        if primelist[p] == True:
            for i in range(p*p, limit+1, p) :
                primelist[i] = False
        p += 1
    return primelist

for _ in range(n) :
    l.append(int(input()))

plist = eratosthenes(max(l))

for e in l:
    cnt = 0
    for k in range(2, int(e/2)+1) :
        if plist[k] == True and plist[e-k] == True:
            cnt += 1
    count.append(cnt)

for element in count :
    print(element)