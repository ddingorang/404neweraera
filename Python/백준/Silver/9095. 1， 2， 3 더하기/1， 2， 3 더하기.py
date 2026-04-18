import sys

n = int(sys.stdin.readline().rstrip())
d = [0 for _ in range(11)]
d[0] = 1
d[1] = 1
d[2] = 2
result = []

for i in range(3, 11) :
    d[i] = d[i-1] + d[i-2] + d[i-3]

for _ in range(n) :
    x = int(sys.stdin.readline().rstrip())
    result.append(d[x])

for e in result :
    print(e)