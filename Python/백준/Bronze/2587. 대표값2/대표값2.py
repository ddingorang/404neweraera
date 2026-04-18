a = [0]*5

for i in range(0, 5) :
    a[i] = int(input(""))
    
a.sort()
avg = int(sum(a) / 5)
print(avg)
print(a[2])
