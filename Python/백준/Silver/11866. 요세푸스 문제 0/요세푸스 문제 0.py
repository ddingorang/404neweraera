import sys
from collections import deque
input1 = sys.stdin.readline().rstrip()
n, k = map(int, input1.split(" "))
stack = deque()
result = []

for i in range(1, n+1) :
    stack.append(i)

while 1 :
    if len(result) == n : break
    for _ in range(k - 1) :
        stack.append(stack.popleft())
    result.append(stack.popleft()) # k번째 인건 pop

i = 1
print("<", end="")
for element in result :
    if i == len(result) :
        print(f'{element}>', end="")
    else :
        print(f'{element}, ', end="")
    i += 1
