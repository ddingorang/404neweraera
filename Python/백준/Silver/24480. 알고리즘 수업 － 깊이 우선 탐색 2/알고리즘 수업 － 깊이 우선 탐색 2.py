import sys
from collections import defaultdict
sys.setrecursionlimit(10**7)
input1 = sys.stdin.readline().rstrip()
n, m, r = map(int, input1.split(" "))
visited = [0]*n
graph = defaultdict(list)
order = 1
orderlist = [0]*n

def dfs(node, visited) :
    global order
    visited[node-1] = 1
    orderlist[node-1] = order
    order += 1
    for neighbor in graph.get(node, []) :
        if visited[neighbor-1] == 0 :
            dfs(neighbor, visited)

for i in range(m) :
    input2 = sys.stdin.readline().rstrip()
    a, b = map(int, input2.split(" "))
    graph[a].append(b)
    graph[b].append(a)

for key in graph :
    graph[key].sort(reverse=True)

dfs(r, visited)

for element in orderlist :
    print(element)

