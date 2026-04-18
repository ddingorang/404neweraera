n = int(input(''))
start = 3
for i in range(n-1) :
    start += (start - 1)

print(start**2)