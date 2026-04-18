import sys

a, b = map(int, sys.stdin.readline().split(' '))

tmpa, tmpb = a, b
while tmpb != 0:
    tmpa, tmpb = tmpb, tmpa % tmpb

print(tmpa)
print(int(a*b/tmpa))