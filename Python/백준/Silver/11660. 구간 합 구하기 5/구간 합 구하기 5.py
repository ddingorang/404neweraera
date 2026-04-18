import sys

n, m = map(int, sys.stdin.readline().split(' '))
t = []
d = [[0 for _ in range(n+1)] for _ in range(n+1)]
result = []
for _ in range(n) :
    t.append(list(map(int, sys.stdin.readline().split(' '))))

d[1][1] = t[0][0]
for i in range(2, n+1) :
    d[1][i] = d[1][i-1] + t[0][i-1]
for j in range(2, n+1) :
    d[j][1] = d[j-1][1] + t[j-1][0]

for k in range(2, n+1) :
    for l in range(2, n+1) :
        d[k][l] = d[k-1][l] + d[k][l-1] - d[k-1][l-1] + t[k-1][l-1]

for _ in range(m) :
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split(' '))
    s = d[x2][y2] - d[x1-1][y2] - d[x2][y1-1] + d[x1-1][y1-1]
    result.append(s)

for e in result :
    print(e)