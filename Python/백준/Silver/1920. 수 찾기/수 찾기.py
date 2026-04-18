import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
numlist = list(map(int, input().rstrip().split(" ")))
m = int(input())
findlist = list(map(int, input().rstrip().split(" ")))

numlist.sort()

for e in findlist :
    found = False
    start = 0
    end = len(numlist)-1
    while start <= end :
        midi = int((start+end)//2)
        midv = numlist[midi]
        if midv > e :
            end = midi - 1
        elif midv < e :
            start = midi + 1
        else :
            found = True
            break

    if found :
        print(1)
    else :
        print(0)