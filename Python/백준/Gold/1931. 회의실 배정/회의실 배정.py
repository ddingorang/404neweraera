import sys
input = sys.stdin.readline
time = []

n = int(input())
for _ in range(n) :
    a, b = map(int, input().split(" "))
    time.append((a, b))

time.sort(key=lambda x : (x[1], x[0]))
start = time[0][0]
end = time[0][1]
count = 1

for i in range(1, len(time)) :
    if time[i][0] < end : continue
    else :
        start = time[i][0]
        end = time[i][1]
        count += 1

print(count)