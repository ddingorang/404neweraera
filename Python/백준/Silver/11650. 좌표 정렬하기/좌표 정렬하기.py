testnum = int(input(""))
pt = [0]*testnum

for i in range(testnum) :
    pt[i] = tuple(map(int, input("").split(" ")))

pt.sort()
for j in range(testnum) :
    print("{} {}".format(pt[j][0], pt[j][1]))