import sys
input = sys.stdin.readline

datanum, querynum = map(int, input().split(" "))
data = list(map(int, input().split(" ")))
sum = [0]
result = []
temp = 0

for i in range(0, datanum) :
    temp += data[i]
    sum.append(temp)

for _ in range(0, querynum) :
    a, b = map(int, input().split(" "))
    result.append(sum[b] - sum[a-1])

for element in result :
    print(element)