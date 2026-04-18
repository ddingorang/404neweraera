import sys

result = []
while 1:
    n = list(map(int, sys.stdin.readline().split(' ')))
    if n[0] == 0 and n[1] == 0 and n[2] == 0 : break
    square = list(map(lambda x : x**2, n))
    square.sort()
    if square[0] + square[1] == square[2]:
        result.append('right')
    else :
        result.append('wrong')

for e in result :
    print(e)