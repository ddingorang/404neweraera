triangle = list(map(int, input("").split()))
maxindex = 0
while 1:
    for i, element in enumerate(triangle) :
        if max(triangle) == triangle[i] : maxindex = i
    if triangle[maxindex] < sum(triangle) - triangle[maxindex] : break
    triangle[maxindex] -= 1

print(sum(triangle))