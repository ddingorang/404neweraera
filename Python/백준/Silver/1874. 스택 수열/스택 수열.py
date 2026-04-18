import sys
input = sys.stdin.readline

possible = True
n = int(input())
numlist = []
s = []
r = []
m = 1

for i in range(n) :
    numlist.append(int(input()))

for element in numlist :
    if element >= m :
        while element >= m :
            s.append(m)
            r.append('+')
            m += 1
        s.pop()
        r.append('-')
    else :
        x = s.pop()
        if x > element :
            print('NO')
            possible = False
            break
        r.append('-')

if possible == True :
    for e in r :
        print(e)
