n = int(input(""))
paper = [[0 for column in range(100)] for row in range(100)]

for _ in range(n) :
    x, y = map(int, input("").split())
    for j in range(y, y+10) :
        for i in range(x, x + 10):
            paper[100-j-1][i-1] = 1

total = 0
for element in paper :
    total += sum(element)

print(total)