import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m = map(int, input().rstrip().split(" "))
miro = [[0]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]

for i in range(n) :
    line = list(input().rstrip())
    for j in range(m) :
        miro[i][j] = int(line[j])

def bfs(i, j) :
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    while q :
        now = q.popleft()
        for k in range(4) :
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if x>=0 and y>=0 and x<n and y<m :
                if not visited[x][y] and miro[x][y] != 0:
                    visited[x][y] = True
                    miro[x][y] = miro[now[0]][now[1]] + 1
                    q.append((x, y))

bfs(0, 0)
print(miro[n-1][m-1])