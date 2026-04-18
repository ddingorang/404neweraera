testnum = int(input(""))
pt = [0]*testnum

for i in range(testnum) :
    pt[i] = list(tuple(map(int, input("").split(" "))))
    pt[i][0], pt[i][1] = pt[i][1], pt[i][0]

pt.sort()
for j in range(testnum) :
    print("{} {}".format(pt[j][1], pt[j][0]))

