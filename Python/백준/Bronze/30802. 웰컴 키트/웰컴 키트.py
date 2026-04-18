import sys

n = int(sys.stdin.readline().rstrip())
tshirts = list(map(int, sys.stdin.readline().split(' ')))
t, p = map(int, sys.stdin.readline().split(' '))
result = []
tset = 0
pset = 0
pleft = 0
for e in tshirts :
    tset += (e-1) // t + 1

pset = n // p
pleft = n % p

print(tset)
print(pset, pleft)