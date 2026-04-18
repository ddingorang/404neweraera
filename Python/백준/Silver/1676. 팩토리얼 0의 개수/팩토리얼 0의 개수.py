import sys

n = int(sys.stdin.readline().rstrip())

two = 0
five = 0
for i in range(n, 0, -1) :
    temp = i
    while temp % 5 == 0:
        temp /= 5
        five += 1
    while temp % 2 == 0:
        temp /= 2
        two += 1

print(min(two, five))