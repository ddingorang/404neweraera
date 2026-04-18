import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())
r = []
for _ in range(t) :
    h, w = map(int, sys.stdin.readline().rstrip().split(' '))
    grid = []
    q = deque()
    count = 0
    visited = [[0 for _ in range(w)] for _ in range(h)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for _ in range(h) :
        row = list(sys.stdin.readline().rstrip())
        grid.append(row)
    for i in range(h) :
        for j in range(w) :
            if visited[i][j] == 0 and grid[i][j] == '#':
                q.append((i, j))
                visited[i][j] = 1
                while q:
                    curi, curj = q.popleft()
                    for k in range(4) :
                        ni = curi + dy[k]
                        nj = curj + dx[k]
                        if 0<=ni<h and 0<=nj<w :
                            if visited[ni][nj] == 0 and grid[ni][nj] == '#' :
                                q.append((ni, nj))
                                visited[ni][nj] = 1
                count += 1
    r.append(count)

for e in r :
    print(e)
