import sys

n = list(map(int, sys.stdin.readline().rstrip().split(' ')))
s = 0
for e in n :
    mul = e * e
    s += mul

print(s % 10)