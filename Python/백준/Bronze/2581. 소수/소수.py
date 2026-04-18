a = int(input(""))
b = int(input(""))
prlist = []

for i in range(a, b+1) :
    for j in range(1, i) :
        if i == 2 : 
            prlist.append(2)
            continue
        if j == 1: 
            continue
        elif i % j == 0 :
            break
        elif j == i-1 :
            prlist.append(i)
         
    
if len(prlist) == 0 :
    print(-1)
else :
    print(sum(prlist))
    print(min(prlist))