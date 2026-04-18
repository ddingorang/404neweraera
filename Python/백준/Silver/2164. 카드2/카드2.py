import sys
from collections import deque
input1 = int(sys.stdin.readline())
n = input1
stack = deque()
result = []

for i in range(1, n+1) :
    stack.append(i)

while len(stack) > 1 :
    stack.popleft()
    if len(stack) == 1 : break
    stack.append(stack.popleft())

print(stack.popleft()) # 마지막으로 남은 원소

for element in result :
    print(element)