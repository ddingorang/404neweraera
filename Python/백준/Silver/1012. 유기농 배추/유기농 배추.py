import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())
result = []
for _ in range(t) :
    m, n, k = map(int, sys.stdin.readline().split(' '))
    field = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split(' '))
        field[y][x] = 1
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    q = deque()
    count = 0
    for x in range(m) :
        for y in range(n) :
            if field[y][x] == 1 and visited[y][x] == 0 :
                q.append((y, x))
                visited[y][x] = 1
                while q:
                    cur = q.popleft()
                    for i in range(4) :
                        my = cur[0] + dy[i]
                        mx = cur[1] + dx[i]
                        if mx >= 0 and mx < m and my >= 0 and my < n:
                            if visited[my][mx] == 0 and field[my][mx] == 1:
                                q.append((my, mx))
                                visited[my][mx] = 1
                count += 1
    result.append(count)

for e in result :
    print(e)