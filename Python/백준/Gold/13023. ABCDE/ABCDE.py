import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split(" "))
adjlist = [[] for _ in range(n)]
visited = [0 for _ in range(n)]
possible = 0

def dfs(x, depth) :
    global possible
    if depth == 5 :
        possible = 1
        return
    visited[x] = 1
    for j in adjlist[x] :
        if visited[j] == 0 :
            dfs(j, depth + 1)
    visited[x] = 0

for _ in range(m) :
    a, b = map(int, input().split(" "))
    adjlist[a].append(b)
    adjlist[b].append(a)

for i in range(n) :
    dfs(i, 1)
    if possible : break

print(possible)