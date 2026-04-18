stulist = []
absentlist = []
for i in range(28) : 
    stulist.append(input(""))

for j in range(1, 31) :
    if str(j) not in stulist :
        absentlist.append(j)

print(absentlist[0])
print(absentlist[1])