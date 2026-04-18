import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = list(map(int, input().split()))

# 정렬 하고
arr.sort()
start = 0
end = n-1
cnt = 0

while start < end :
    if arr[start] + arr[end] < m :
        start += 1
    elif arr[start] + arr[end] > m :
        end -= 1
    elif arr[start] + arr[end] == m :
        start +=1
        end -= 1
        cnt += 1

print(cnt)
