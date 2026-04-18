import math
testnum = int(input(""))
h = [0]*testnum
w = [0]*testnum
n = [0]*testnum
floor = [0]*testnum
roomnum = [0]*testnum

for i in range(testnum) :
    h[i], w[i], n[i] = list(tuple(map(int, input("").split())))
    if n[i] % h[i] == 0 :
        floor[i] = h[i]
    else :
        floor[i] = n[i] % h[i]
    roomnum[i] = math.ceil(n[i] / h[i])

for i in range(testnum) :
    if roomnum[i] < 10 : 
        print("{}{:02d}".format(floor[i], roomnum[i]))
    else :
        print("{}{}".format(floor[i], roomnum[i]))

