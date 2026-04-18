import sys
from collections import deque
input = sys.stdin.readline

n, m, st = map(int, input().split(" "))
adjlist = [[] for _ in range(n+1)]
for _ in range(m) :
    s, e = map(int, input().rstrip().split(" "))
    adjlist[s].append(e)
    adjlist[e].append(s)

for i in range(n+1) :
    adjlist[i].sort()

def dfs(x) :
    print(x, end=' ')
    visited1[x] = True
    for i in adjlist[x] :
        if not visited1[i] :
            dfs(i)

visited1 = [False]*(n+1)
dfs(st)

def bfs(x) :
    queue = deque()
    queue.append(x)
    visited2[x] = True
    while queue :
        now = queue.popleft()
        print(now, end = ' ')
        for i in adjlist[now] :
            if not visited2[i] :
                visited2[i] = True
                queue.append(i)

print()
visited2 = [False]*(n+1)
bfs(st)