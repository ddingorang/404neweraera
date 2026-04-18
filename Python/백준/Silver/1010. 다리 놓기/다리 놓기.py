import math

n = int(input(''))
result = []
for _ in range(n):
    # 조합(kCn)
    n, k = tuple(map(int, input('').split(' ')))
    result.append(math.comb(k, n))

for e in result:
    print(e)