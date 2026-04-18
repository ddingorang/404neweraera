import sys
from collections import defaultdict, deque

n, m, r = map(int, sys.stdin.readline().rstrip().split(' '))
visited = [0 for _ in range(n+1)]
friends = defaultdict(list)
q = deque()

for _ in range(m) : # 인접 리스트
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    friends[a].append(b)
    friends[b].append(a)

for e in friends :
    friends[e].sort(reverse=True)

q.append(r)
result = [0 for _ in range(n+1)]
count = 1
result[r] = 1
while q :
    curi = q.popleft()
    visited[curi] = 1

    for e in friends[curi] :
        if visited[e] == 0 :
            visited[e] = 1
            q.append(e)
            count += 1
            result[e] = count

for i in range(1, len(result)) :
    print(result[i])