
from collections import deque
import sys
input1 = int(sys.stdin.readline())

n = int(input1)
q = deque()
action = []

for i in range(n) :
    input2 = str(sys.stdin.readline().rstrip())
    action.append(input2)

for e in action :
    if e[:4] == 'push' :
        a, b = e.split(" ")
        q.append(b)
    elif e == 'pop' :
        if len(q) == 0 :
            print(-1)
        else :
            print(q.popleft())
    elif e == 'size' :
        print(len(q))
    elif e == 'empty' :
        if len(q) == 0 : print(1)
        else : print(0)
    elif e == 'front' :
        if len(q) == 0 :
            print(-1)
        else :
            print(q[0])
    elif e == 'back' :
        if len(q) == 0 :
            print(-1)
        else :
            print(q[-1])

