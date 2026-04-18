import sys
import heapq
n = int(sys.stdin.readline().rstrip())
pq = []
result = []
for _ in range(n) :
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if len(pq) == 0:
            result.append((0, 0))
        else :
            result.append(heapq.heappop(pq))
    elif x < 0:
        heapq.heappush(pq, (-x, x))
    elif x > 0:
        heapq.heappush(pq, (x, x))

for e in result :
    print(e[1])