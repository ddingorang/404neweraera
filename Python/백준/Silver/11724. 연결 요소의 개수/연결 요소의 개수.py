import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, e = map(int, input().split(" "))
adjlist = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
count = 0

def dfs(x) :
    visited[x] = 1
    for k in adjlist[x] :
        if visited[k] == 0 :
            dfs(k)

for i in range(e) :
    a, b = map(int, input().split(" "))
    adjlist[a].append(b)
    adjlist[b].append(a)

for j in range(1, n+1) :
    if visited[j] == 0 :
        count += 1
        dfs(j)

print(count)