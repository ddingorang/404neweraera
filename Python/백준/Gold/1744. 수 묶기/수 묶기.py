import sys
from queue import PriorityQueue
input = sys.stdin.readline

minus = PriorityQueue()
plus = PriorityQueue()
zero = 0
oone = 0
sum = 0

n = int(input())
for _ in range(n) :
    num = int(input())
    if num < 0 : minus.put(num)
    elif num == 0 : zero += 1
    elif num > 1 : plus.put(num*(-1))
    elif num == 1 : oone += 1

while minus.qsize() > 1 :
    one = minus.get()
    two = minus.get()
    sum += one * two

if minus.qsize() > 0 :
    if zero == 0 :
        sum += minus.get()

while plus.qsize() > 1:
    one = plus.get() * (-1)
    two = plus.get() * (-1)
    sum += one * two

if plus.qsize() > 0 :
    sum += plus.get() * (-1)

sum += oone
print(sum)