n = int(input())

ppl = []
for _ in range(n) :
    x, y = map(int, input().split(' '))
    ppl.append((x, y))

result = []
for i in range(n) :
    count = 1
    for j in range(n) :
        if i == j : continue
        if ppl[j][0] > ppl[i][0]  and ppl[j][1] > ppl[i][1] :
            count += 1
    result.append(count)

for e in result:
    print(f'{e} ', end='')