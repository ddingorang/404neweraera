arr = [[]*9 for i in range(9)]
max = 0
row = 0
col = 0

for j in range(9) :
    arr[j] = input("").split(" ")
    arr[j] = list(map(int, arr[j]))
    
for k in range(9) :
    for l in range(9) :
        if arr[k][l] > max : 
            max = arr[k][l]
            row = k
            col = l

print(max)
print("{} {}".format(row+1, col+1))
    

