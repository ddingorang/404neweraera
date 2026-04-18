ul = list(map(int, input().split(' ')))
st = list(map(int, input().split(' ')))

uls = 0
sts = 0
isleading = False
for i in range(9):
    uls += ul[i]
    if uls > sts :
        isleading = True
    sts += st[i]

if isleading :
    print("Yes")
else :
    print("No")