testnum = int(input(""))
num = list(map(int, input("").split(" ")))
prnum = 0

for i in range(testnum) :
    for j in range(1, num[i]) :
        if j == 1 :
            if num[i] == 2 : prnum += 1
            continue
        elif num[i] % j == 0 :
            break
        elif j == num[i]-1 :
            prnum += 1
        
print(prnum)