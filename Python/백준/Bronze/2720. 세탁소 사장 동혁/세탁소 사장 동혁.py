import sys

n = int(sys.stdin.readline().rstrip())
result = []
for _ in range(n) :
    c = int(sys.stdin.readline().rstrip())
    q=0
    d=0
    n=0
    p=0
    while c >= 25 :
        q += 1
        c -= 25
    while c >= 10 :
        d += 1
        c -= 10
    while c >= 5 :
        n += 1
        c -= 5
    while c >= 1 :
        p += 1
        c -= 1
    r = f'{q} {d} {n} {p}'
    result.append(r)

for e in result :
    print(e)