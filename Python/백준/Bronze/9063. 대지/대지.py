n = int(input(""))
x = []
y = []
for _ in range(n) :
    a, b = map(int, input("").split())
    x.append(a)
    y.append(b)

if n == 1 : area = 0
else :
    xmax, xmin = max(x), min(x)
    ymax, ymin = max(y), min(y)
    area = (xmax - xmin) * (ymax - ymin)

print(area)