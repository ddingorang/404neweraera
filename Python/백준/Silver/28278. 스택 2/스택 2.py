import sys
from collections import deque
input1 = int(sys.stdin.readline())
n = input1
stack = deque()
result = []

for i in range(n) :
    input2 = sys.stdin.readline().rstrip()
    a = input2
    if a[0] == '1' :
        b, c = a.split(" ")
        stack.append(c)
    elif a == '2' :
        if len(stack) == 0 : result.append(-1)
        else : result.append(stack.pop())
    elif a == '3' :
        result.append(len(stack))
    elif a == '4' :
        if len(stack) == 0 : result.append(1)
        else : result.append(0)
    elif a == '5' :
        if len(stack) == 0 : result.append(-1)
        else : result.append(stack[len(stack)-1])

for element in result :
    print(element)