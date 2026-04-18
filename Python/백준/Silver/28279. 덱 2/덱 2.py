import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
q = deque()
for _ in range(n) :
    cmd = sys.stdin.readline().rstrip()
    if cmd[0] == '1':
        c, n = map(int, cmd.split(' '))
        q.appendleft(n)
    elif cmd[0] == '2' :
        c, n = map(int, cmd.split(' '))
        q.append(n)
    elif cmd[0] == '3' :
        if len(q) == 0 :
            print(-1)
        else :
            print(q.popleft())
    elif cmd[0] == '4' :
        if len(q) == 0 :
            print(-1)
        else :
            print(q.pop())
    elif cmd[0] == '5' :
        print(len(q))
    elif cmd[0] == '6' :
        if len(q) == 0:
            print(1)
        else :
            print(0)
    elif cmd[0] == '7' :
        if len(q) == 0 :
            print(-1)
        else :
            print(q[0])
    elif cmd[0] == '8' :
        if len(q) == 0 :
            print(-1)
        else :
            print(q[len(q)-1])