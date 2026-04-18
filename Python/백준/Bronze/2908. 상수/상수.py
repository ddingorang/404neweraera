a = input("").split()
afterswitch = [0] * 2
x = 0
y = 0

for i in range(2) :
    x = int(a[i][0])
    y = int(a[i][2])
    afterswitch[i] = int(a[i]) - (100*(x-y) + (y-x))

print(max(afterswitch))

