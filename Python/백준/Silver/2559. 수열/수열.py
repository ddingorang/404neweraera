import sys

n, k = map(int, sys.stdin.readline().split(' '))
t = list(map(int, sys.stdin.readline().split(' ')))

front = 0
rear = k-1
max = float('-inf')
s = sum(t[front : rear+1])
while 1:
    if s > max :
        max = s
    s -= t[front]
    front += 1
    rear += 1
    if rear == len(t) : break
    s += t[rear]
print(max)