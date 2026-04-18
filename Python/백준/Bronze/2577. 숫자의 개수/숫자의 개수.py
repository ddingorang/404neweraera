import sys

n = []
for _ in range(3):
    x = int(sys.stdin.readline().rstrip())
    n.append(x)

m = n[0]*n[1]*n[2]
cnt = [0 for _ in range(10)]
for e in list(str(m)) :
    cnt[int(e)] += 1

for elm in cnt :
    print(elm)
